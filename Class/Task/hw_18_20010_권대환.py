from tkinter import *
import random
import time


def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb


app = Tk()
app.title("Bouncing Ball")

canvas = Canvas(app, width=500, height=500)
canvas.pack()
canvas.update()


class Ball:
    def __init__(self):
        self.size = random.randint(20, 70)
        self.color = random.randint(0, 8)
        self.direction = [random.random()*5, random.random()*5]
        self.id = canvas.create_oval(0, 0, self.size, self.size,
                                     fill=_from_rgb((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))))
        self.canvas_height = canvas.winfo_height()
        self.canvas_width = canvas.winfo_width()

    def move(self):
        ball_pos = canvas.coords(self.id)
        if ball_pos[0]+self.size > self.canvas_width or ball_pos[0] < 0:
            self.direction[0] *= -1
        if ball_pos[1]+self.size > self.canvas_height or ball_pos[1] < 0:
            self.direction[1] *= -1
        canvas.move(self.id, *self.direction)


num = random.randint(5, 10)
balls = [Ball() for _ in range(num)]
run = True


def window_exit():
    global run
    run = False


app.protocol("WM_DELETE_WINDOW", window_exit)


while run:
    app.update()
    time.sleep(0.01)
    for ball in balls:
        ball.move()

app.destroy()
