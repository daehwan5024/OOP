from cs1robots import *
load_world('../worlds/ex36.rur.wld')
gshs = Robot()
gshs.set_trace(color='blue')
beepers = []
gshs.move()
while True:
    num_of_beeper = 0
    while gshs.on_beeper():
        num_of_beeper += 1
        gshs.pick_beeper()
    beepers.append(num_of_beeper)
    if not gshs.front_is_clear():
        break
    gshs.move()
beepers.sort()
gshs.turn_left()
gshs.turn_left()
for i in beepers:
    for __ in range(0, i):
        gshs.drop_beeper()
    gshs.move()
