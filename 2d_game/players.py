from uuid import uuid4


class Vec2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2D(self.x - other.x, self.y - other.y)


class Player:
    def __init__(self):
        self.player_id = uuid4()
        self.pos = Vec2D(10, 10)

    def move_up(self):
        return self.pos - Vec2D(0, 1)

    def move_down(self):
        return self.pos + Vec2D(0, 1)

    def move_left(self):
        return self.pos - Vec2D(1, 0)

    def move_right(self):
        return self.pos + Vec2D(1, 0)
