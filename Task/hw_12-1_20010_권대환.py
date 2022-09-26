import turtle
import colorsys
screen = turtle.Screen()
screen.bgcolor('black')

screen.tracer(0)
screen.colormode(255)
thickness = 20
top = 200
size = 8
disk_size = 20
speed = 5


class Disc:
    def __init__(self, n, x, y):
        self.n = n
        self.x = x
        self.y = y
        self.width = n * disk_size
        (h, s, v) = (179 / size * (n-1), 255, 255)
        (h, s, v) = (h / 179, s / 255, v / 255)
        (r, g, b) = colorsys.hsv_to_rgb(h, s, v)
        self.color = (int(r * 255), int(g * 255), int(b * 255))
        self.drawer = turtle.Turtle(visible=False)
        self.drawer.width = 0

    def draw(self):
        self.drawer.color(*self.color)
        self.drawer.fillcolor(*self.color)
        self.drawer.penup()
        self.drawer.goto(self.x - self.width / 2, self.y + thickness / 2)
        self.drawer.pendown()
        self.drawer.begin_fill()
        self.drawer.setheading(0)
        self.drawer.forward(self.width)
        self.drawer.setheading(-90)
        self.drawer.forward(thickness)
        self.drawer.setheading(-180)
        self.drawer.forward(self.width)
        self.drawer.setheading(90)
        self.drawer.forward(thickness)
        self.drawer.end_fill()
        screen.update()

    def change_x(self, x):
        if self.x > x:
            for i in range(self.x, x-1, -speed):
                self.drawer.clear()
                self.x = i
                self.draw()
        else:
            for i in range(self.x, x+1, speed):
                self.drawer.clear()
                self.x = i
                self.draw()

    def change_y(self, y):
        if self.y > y:
            for i in range(self.y, y-1, -speed):
                self.drawer.clear()
                self.y = i
                self.draw()
        else:
            for i in range(self.y, y+1, speed):
                self.drawer.clear()
                self.y = i
                self.draw()

    def move_to(self, x, y):
        self.drawer.clear()
        self.change_y(top)
        self.change_x(x)
        self.change_y(y)

    def move_direct(self, x, y):
        self.x = x
        self.y = y
        self.drawer.clear()
        self.draw()


class Tower(list):
    def __init__(self, x):
        super().__init__()
        self.x = x

    def append1st(self, current_disc):
        super().append(current_disc)
        current_disc.move_direct(self.x, (len(self)+1) * 20 - 100)

    def append(self, current_disc):
        super().append(current_disc)
        current_disc.move_to(self.x, (len(self)+1) * 20 - 100)

    def pop(self):
        curren_disc = super().pop()
        return curren_disc


def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        c.append(a.pop())
        hanoi(n-1, b, a, c)


def main(*_):
    screen.onclick(None)
    hanoi(size, t1, t2, t3)
    screen.exitonclick()


if __name__ == "__main__":
    t1 = Tower(-200)
    t2 = Tower(0)
    t3 = Tower(200)
    for i in range(size, 0, -1):
        t1.append1st(Disc(i, t1.x, (size-i) * 20 - 100))
    screen.onclick(main)
    screen.mainloop()
