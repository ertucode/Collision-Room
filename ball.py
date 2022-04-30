from dataclasses import dataclass
import pygame
import math
import random as r
from vars import *
from kd_tree import *
import numpy as np
from vector import Vector2

@dataclass
class Ball:
    center : Vector2
    radius: int or float
    color: str or tuple
    velocity: Vector2

    def __post_init__(self):
        self.mass = self.radius ** 2

    def draw(self, win):
        pygame.draw.circle(win, self.color, self.center, self.radius)

    def move(self):
        self.center += self.velocity

    def handle_collision_with_walls(self):
        if self.center.x < self.radius:
            self.center.x = abs(self.radius - self.center.x) + self.radius
            self.velocity **= (-1, 1)
        elif self.center.x > WIDTH - self.radius:
            self.center.x = WIDTH - self.radius - abs(WIDTH - self.radius - self.center.x)
            self.velocity **= (-1, 1)

        if self.center.y < self.radius:
            self.center.y = abs(self.radius - self.center.y) + self.radius
            self.velocity **= (1, -1)
        elif self.center.y > HEIGHT - self.radius:
            self.center.y = HEIGHT - self.radius - abs(HEIGHT - self.radius - self.center.y)
            self.velocity **= (1, -1)


    def handle_collision_with_other_ball(self, other):
        dist = abs(self.center - other.center)
        if dist * 0.96 <= (self.radius + other.radius):
            self.velocity, other.velocity = self.get_response_velocities(other)

            while self.is_on_top_of_other_ball(other):
                self.center += (self.center - other.center) * 0.1

    def is_on_top_of_other_ball(self, other):
        return (abs(self.center - other.center)) <= (self.radius + other.radius)
    
    def get_response_velocities(self, other):
        # https://en.wikipedia.org/wiki/Elastic_collision
        v1 = self.velocity
        v2 = other.velocity
        m1 = self.mass
        m2 = other.mass
        x1 = self.center
        x2 = other.center

        def compute_velocity(v1, v2, m1, m2, x1, x2):
            return v1 - (2 * m2 / (m1 + m2)) *(v1 - v2) *  (x1 - x2) / abs(x1 - x2) ** 2 * (x1 - x2)

        ball_response_v = compute_velocity(v1, v2, m1, m2, x1, x2)
        other_response_v = compute_velocity(v2, v1, m2, m1, x2, x1)
        return ball_response_v, other_response_v

    @property
    def left(self):
        return self.center.x - self.radius

    @property
    def right(self):
        return self.center.x + self.radius


class BallHandler:
    def __init__(self):
        self.balls = []
        self.method = SolveMethod.naive

    def spawn_random_balls(self, count = 1, size = (5,40)):
        for _ in range(count):
            ball = Ball(Vector2(r.randrange(10, WIDTH - 10), r.randrange(10, HEIGHT - 10)), r.randrange(*size), r.choice(colors), Vector2.from_angle(r.uniform(0, 2 * math.pi)))
            if self.balls:
                colliding_with_others = True
                while colliding_with_others:
                    colliding_with_others = False
                    for other in self.balls:
                        if ball.is_on_top_of_other_ball(other):
                            ball.center.x, ball.center.y = (r.randrange(10, WIDTH - 10), r.randrange(10, HEIGHT - 10))
                            colliding_with_others = True
                            break
            self.balls.append(ball)
                
            

    def spawn_ball(self, center, radius, color, direction):
        self.balls += [Ball(center, radius, color, direction)]

    def draw_and_move_balls(self, win):
        if self.balls:
            for ball in self.balls:
                ball.move()
                ball.draw(win)
                ball.handle_collision_with_walls()

            if self.method == SolveMethod.naive:
                self.handle_collision_between_balls_naive()
            elif self.method == SolveMethod.sweep:
                self.handle_collision_between_balls_sweep_and_prune()



    def handle_collision_between_balls_naive(self):
        for i in range(len(self)):
            for j in range(i + 1, len(self)):
                self.balls[i].handle_collision_with_other_ball(self.balls[j])

    def handle_collision_between_balls_sweep_and_prune(self):
        self.balls.sort(key = lambda ball: ball.center.x - ball.radius)
        active_list = []
        active_interval = Vector2(self.balls[0].left, self.balls[0].right)
        possible_collisions = []
        for ball in self.balls:
            to_remove = [active_ball for active_ball in active_list if ball.left > active_ball.right]

            for r in to_remove:
                active_list.remove(r)

            for other_ball in active_list:
                possible_collisions.append((ball, other_ball))

            active_list.append(ball)
        
        for possible_collision in possible_collisions:
            possible_collision[0].handle_collision_with_other_ball(possible_collision[1])


    def delete_balls(self, count):
        if count >= len(self):
            for i in reversed(range(len(self))):
                del self.balls[i]
        else:
            indexes = r.sample(range(len(self)), count)
            for i, ind in enumerate(indexes):
                del self.balls[i - ind]

    def __len__(self):
        return len(self.balls)

        


