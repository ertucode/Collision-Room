import pygame
from vars import *
from ball import BallHandler
from vector import Vector2

pygame.init()

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision room")

def draw(win, ball_handler):
    win.fill("black")

    ball_handler.draw_and_move_balls(win)

    pygame.display.update()

print()

def main(FPS):
    run = True
    clock = pygame.time.Clock()

    ball_handler = BallHandler()

    ball_handler.spawn_ball(Vector2(500, 200), 50, "white", Vector2.from_angle(1.2))
    ball_handler.spawn_ball(Vector2(200, 500), 20, "yellow", Vector2.from_angle(0.5))
    ball_handler.spawn_ball(Vector2(800, 200), 30, "blue", Vector2.from_angle(0.2))
    ball_handler.spawn_ball(Vector2(300, 300), 10, "red", Vector2.from_angle(1.5))

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ball_handler.spawn_random_balls(10, (5,40))
                elif event.key == pygame.K_DELETE:
                    ball_handler.delete_balls(10)
                elif event.key == pygame.K_KP_PLUS:
                    FPS += 10
                elif event.key == pygame.K_KP_MINUS:
                    FPS = max(FPS - 10, 10)
                elif event.key == pygame.K_UP:
                    ball_handler.method = SolveMethod.naive
                elif event.key == pygame.K_DOWN:
                    ball_handler.method = SolveMethod.sweep


        print("\r", end="")
        print(f" FPS = {clock.get_fps():.2f}, MAX = {FPS} , method = {ball_handler.method.name}", end="  ")
   
        draw(win, ball_handler)

    pygame.quit()

if __name__ == "__main__":
    main(FPS)