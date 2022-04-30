import math

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple):
            return Vector2(self.x + other[0], self.y + other[1])
        elif isinstance(other, (float, int)):
            return Vector2(self.x + other, self.y + other)

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        elif isinstance(other, tuple):
            return Vector2(self.x - other[0], self.y - other[1])
        elif isinstance(other, (float, int)):
            return Vector2(self.x - other, self.y - other)

    def __mul__(self, other):
        if isinstance(other, Vector2):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, tuple):
            return self.x * other[0] + self.y * other[1]
        elif isinstance(other, (float, int)):
            return Vector2(self.x * other, self.y * other)

    def __pow__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
        elif isinstance(other, tuple):
            return Vector2(self.x * other[0], self.y * other[1])

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return -self.__sub__(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5  

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __repr__(self):
        return f"Vector2({self.x:.2f},{self.y:.2f})"

    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5 

    def __len__(self):
        return 2

    def __getitem__(self, key):
        if key == 0: return self.x
        elif key == 1: return self.y

    def __rlshift__(self, other):
        return other >= self.x and other <= self.y

    @classmethod
    def from_angle(cls, angle):
        return cls(math.cos(angle), -math.sin(angle))

    