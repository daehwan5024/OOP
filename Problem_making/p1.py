from cs1robots import *
load_world('p1.wld')
robot = Robot()
robot.set_trace('blue')
ans = 0


def get_beeper():
    temp = 0
    while robot.on_beeper():
        robot.pick_beeper()
        temp += 1
    return temp


def run_line():
    temp = 0
    while robot.front_is_clear():
        robot.move()
        temp += get_beeper()
    while not robot.facing_north():
        robot.turn_left()
    if not robot.front_is_clear():
        print(globals().get('ans'))
        exit()
    robot.move()
    temp += get_beeper()
    robot.turn_left()
    if not robot.front_is_clear():
        robot.turn_left()
        robot.turn_left()
    return temp


while True:
    ans += run_line()
