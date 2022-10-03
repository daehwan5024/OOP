from tkinter import *
import tkinter.font
import random
import time


def close_window():
    global running
    running = False
    print("Close game")


app = Tk()
app.title("Simple Game")
app.protocol("WM_DELETE_WINDOW", close_window)
canvas = Canvas(app, width=500, height=500, bg='black')
canvas.pack(padx=50, pady=20)
canvas.update()
font = tkinter.font.Font(family="맑은 고딕", size=30)
scoreboard = Label(app, text='0', font=font)
scoreboard.pack(pady=20)


class Ball:
    def __init__(self, canvas1, paddle1, color):
        self.canvas = canvas1
        self.paddle = paddle1
        self.score = 0
        self.id = self.canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 250, 250)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        return pos[0] <= paddle_pos[2] and pos[2] >= paddle_pos[0] and paddle_pos[3] >= pos[3] >= paddle_pos[1]

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.score += 1
            scoreboard['text'] = self.score
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit(pos):
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3


class Paddle:
    def __init__(self, canvas1, color):
        self.canvas = canvas1
        self.id = canvas1.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 150, 400)

        self.x = 0
        self.y = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind('<Left>', self.turn_left)
        self.canvas.bind('<Right>', self.turn_right)
        self.canvas.focus_set()

    def turn_left(self, event):
        self.x = -5

    def turn_right(self, event):
        self.x = 5

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        paddle_pos = self.canvas.coords(self.id)
        if paddle_pos[0] <= 0:
            self.x = 0
        if paddle_pos[2] >= self.canvas_width:
            self.x = 0


paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')
running = True
while running:
    if not running:
        break
    if not ball.hit_bottom:
        ball.draw()
        paddle.draw()
        app.update()
        time.sleep(0.01)
        continue
    break
print(ball.score)
app.destroy()
