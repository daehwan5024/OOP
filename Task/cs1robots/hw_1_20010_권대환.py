from cs1robots import *
load_world('../../worlds/hurdles1.wld')
gshs = Robot()
gshs.set_trace('blue')


def turn_right():
    for _ in range(0, 3):
        gshs.turn_left()

for _ in range(0, 4):
    gshs.move()
    gshs.turn_left()
    gshs.move()
    for __ in range(0, 2):
        turn_right()
        gshs.move()
    gshs.turn_left()
gshs.move()
gshs.pick_beeper()
