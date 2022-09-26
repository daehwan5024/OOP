from cs1robots import *


def to_int(input_list):
    return int(input_list[0]), int(input_list[1])


load_world('input_file/p2.wld')
f = open('input_file/input1.in')
avenue_robot, street_robot = to_int(f.readline().split(' '))
avenues, streets = to_int(f.readline().split(' '))
ans = 0
f.close()

robot = Robot(avenue=avenue_robot, street=street_robot)
robot.set_trace('blue')
visited = [[False for _ in range(avenues)]for __ in range(streets)]


def see_north():
    while not robot.facing_north():
        robot.turn_left()


def check(x, y):
    if not(0 <= x < avenues and 0 <= y < streets):
        return False
    return not visited[x][y]


def f(pre_x, pre_y):
    current_beepers = 0
    x, y = robot.get_pos()
    x -= 1
    y -= 1
    visited[x][y] = True
    while robot.on_beeper():
        robot.pick_beeper()
        current_beepers += 1
    see_north()
    if robot.front_is_clear() and check(x, y+1):
        robot.move()
        current_beepers += f(x, y)
    see_north()
    robot.turn_left()
    if robot.front_is_clear() and check(x-1, y):
        robot.move()
        current_beepers += f(x, y)
    see_north()
    robot.turn_left()
    robot.turn_left()
    if robot.front_is_clear() and check(x, y-1):
        robot.move()
        current_beepers += f(x, y)
    see_north()
    robot.turn_left()
    robot.turn_left()
    robot.turn_left()
    if robot.front_is_clear() and check(x+1, y):
        robot.move()
        current_beepers += f(x, y)
    delta_x = pre_x - x
    delta_y = pre_y - y
    see_north()
    if delta_x == 1:
        robot.turn_left()
        robot.turn_left()
        robot.turn_left()
        robot.move()
    elif delta_x == -1:
        robot.turn_left()
        robot.move()
    elif delta_y == 1:
        robot.move()
    elif delta_y == -1:
        robot.turn_left()
        robot.turn_left()
        robot.move()
    return current_beepers


ans += f(avenue_robot-1, street_robot-1)
while robot.carries_beepers():
    robot.drop_beeper()
print(ans)
