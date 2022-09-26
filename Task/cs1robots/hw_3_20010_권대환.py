from cs1robots import *
load_world('../../worlds/finalMaze.wld')
gshs = Robot()
gshs.set_trace(color='blue')
while not gshs.on_beeper():
    if gshs.right_is_clear():
        gshs.turn_left()
        gshs.turn_left()
        gshs.turn_left()
        gshs.move()
    elif gshs.front_is_clear():
        gshs.move()
    elif gshs.left_is_clear():
        gshs.turn_left()
        gshs.move()
    else:
        gshs.turn_left()
        gshs.turn_left()
        gshs.move()
gshs.pick_beeper()
