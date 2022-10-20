from cs1robots import *


class Disc:
    def __init__(self, n, x, y):
        self.n = n
        self.x = x
        self.y = y


class Tower(list):
    def __init__(self, x):
        super().__init__()
        self.x = x

    def push(self, current_disc):
        self.append(current_disc)
        current_disc.x = self.x
        current_disc.y = len(self) + 1
        import cs1robots
        gshs._x = current_disc.x
        gshs._y = current_disc.y
        for _ in range(current_disc.n):
            cs1robots._world.add_beeper(gshs._x, gshs._y)
        pause(0.1)
        gshs._refresh()

    def pop(self):
        curren_disc = super().pop()
        gshs._x = curren_disc.x
        gshs._y = curren_disc.y
        for i in range(curren_disc.n):
            gshs.pick_beeper()
        pause(0.1)
        return curren_disc


def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        pause(0.1)
        c.push(a.pop())
        pause(0.1)
        hanoi(n-1, b, a, c)
        pause(0.1)


create_world()
gshs = Robot(avenue=1, street=10, beepers=10000)
size = 6


def main():
    t1 = Tower(3)
    t2 = Tower(5)
    t3 = Tower(7)

    for i in range(size, 0, -1):
        t1.push(Disc(i, 3, size - i + 1))
        pass
    hanoi(size, t1, t2, t3)


if __name__ == "__main__":
    main()
