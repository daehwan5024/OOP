from cs1robots import *
load_world('../worlds/frank18.wld')
gshs = Robot(color="light_blue", orientation='E', avenue=1, street=1)
gshs.set_trace(color='blue')
gshs2 = Robot(color="green", orientation='E', avenue=1, street=1, beepers=1000)
gshs2.set_trace(color='red')
direction = 'E'
info = []
for i in range(1, 11):
    for j in range(1, 10):
        beeper_num = 0
        while gshs.on_beeper():
            beeper_num += 1
            gshs.pick_beeper()
        gshs.move()
        if beeper_num == 0:
            continue
        j = 11 - j if i % 2 == 0 else j
        info.append([direction, j, i, beeper_num])
    if i == 10:
        break
    if i % 2 == 1:
        gshs.turn_left()
        gshs.move()
        gshs.turn_left()
        direction = 'W'
    else:
        gshs.turn_left()
        gshs.turn_left()
        gshs.turn_left()
        gshs.move()
        gshs.turn_left()
        gshs.turn_left()
        gshs.turn_left()
        direction = 'E'
max_index = None
temp = 0
for i in info:
    if temp < i[3]:
        max_index = i
        temp = i[3]
for _ in range(max_index[1]-1):
    gshs2.move()
gshs2.turn_left()
for _ in range(max_index[2]-1):
    gshs2.move()
for _ in range(max_index[3]):
    gshs2.drop_beeper()
gshs2.move()
