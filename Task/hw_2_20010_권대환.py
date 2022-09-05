from cs1robots import *
load_world('../worlds/harvest1.wld')
gshs = Robot()
gshs.set_trace('blue')


def turn_right():
    for _ in range(0, 3):
        gshs.turn_left()


def forward(x):
    for _ in range(0, x):
        gshs.move()
        gshs.pick_beeper()


def go():
    gshs.pick_beeper()
    forward(5)
    gshs.turn_left()
    gshs.move()
    gshs.pick_beeper()
    gshs.turn_left()
    forward(5)
    turn_right()
    gshs.move()
    turn_right()


gshs.set_pause(1)
gshs.move()
for _ in range(0, 3):
    go()
