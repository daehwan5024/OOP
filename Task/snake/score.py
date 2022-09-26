from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 24, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 250)
        self.refresh_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.refresh_score()

    def refresh_score(self):
        self.write(f"Score: {self.score} ", False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', False, ALIGNMENT, FONT)
        