from cs1robots import *


class Disc:
    def __init__(self, n, x, y):
        self.n = n
        self.x = x
        self.y = y


class Tower(list):
    def __init__(self, x):
        self.x = x

    def push(self, d):
        self.append(d)
        d.x = self.x
        d.y = len(self) + 1
        # 비퍼를 떨어트리기 위해 아래 코드를 이용할 것.
        import cs1robots
        gshs._x = d.x
        gshs._y = d.y
        for _ in range(d.n):
            cs1robots._world.add_beeper(gshs._x, gshs._y)

        pause(0.1)
        gshs._refresh()

    def pop(self):
        d = super().pop()
        gshs._x = d.x
        gshs._y = d.y
        for i in range(d.n):
            gshs.pick_beeper()
        pause(0.1)
        return d


def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        pause(0.1)
        disk = a.pop()
        c.push(disk)
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
