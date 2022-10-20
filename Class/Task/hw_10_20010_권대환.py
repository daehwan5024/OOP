import turtle
drawer = turtle.Turtle()
window = turtle.Screen()
rate = 0.8
branch_angle = 30
drawer.pensize(2)


def draw(line_len, start_pos, angle):
    if line_len < 25:
        return
    drawer.setheading(angle+branch_angle)
    drawer.color('black' if line_len > 30 else 'light green')
    drawer.forward(line_len)
    draw(line_len*rate, drawer.pos(), angle+branch_angle)
    drawer.penup()
    drawer.setposition(start_pos)
    drawer.pendown()
    drawer.setheading(angle-branch_angle)
    drawer.color('black' if line_len > 30 else 'light green')
    drawer.forward(line_len)
    draw(line_len*rate, drawer.pos(), angle-branch_angle)
    drawer.penup()


drawer.setheading(90)
drawer.forward(100)
draw(100*rate, drawer.pos(), 90)
drawer.setposition((0, 0))
drawer.setheading(90)
window.exitonclick()
