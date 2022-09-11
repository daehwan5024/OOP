import turtle
import random

turtles = [turtle.Turtle() for _ in range(50)]
window = turtle.Screen()
window.screensize(1000, 1000)
window.tracer(0)
headings = [0, 90, 180, 270]
window.colormode(255)
finished = False


def end(x: float, y: float):
    global finished
    finished = True


for tur in turtles:
    tur.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
while True:
    for drawer in turtles:
        drawer.forward(10)
        drawer.setheading(headings[random.randint(0, 3)])
    window.onclick(end)
    window.update()
    if finished:
        break
