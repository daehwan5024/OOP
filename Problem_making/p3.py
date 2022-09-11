from cs1robots import *

file = open('input2.in')
input_values = file.readline().split(' ')
avenues = int(input_values[0])
streets = int(input_values[1])
load_world('p2.wld')
ans = 0
robot = None
visited = [[False for _ in range(avenues)]for __ in range(streets)]


def update(list1, list2):
    for _ in list2:
        list1.append(_)


def see_north():
    while not robot.facing_north():
        robot.turn_left()


def check(x, y):
    if not(0 <= x < avenues and 0 <= y < streets):
        return False
    return not visited[x][y]


def f(pre_x, pre_y):
    possible_list = []
    current_beepers = 0
    x, y = robot.get_pos()
    x -= 1
    y -= 1
    visited[x][y] = True
    possible_list.append((x, y))
    while robot.on_beeper():
        robot.pick_beeper()
        current_beepers += 1
    see_north()
    if robot.front_is_clear() and check(x, y+1):
        robot.move()
        return_value = f(x, y)
        current_beepers += return_value[0]
        update(possible_list, return_value[1])
    see_north()
    robot.turn_left()
    if robot.front_is_clear() and check(x-1, y):
        robot.move()
        return_value = f(x, y)
        current_beepers += return_value[0]
        update(possible_list, return_value[1])
    see_north()
    robot.turn_left()
    robot.turn_left()
    if robot.front_is_clear() and check(x, y-1):
        robot.move()
        return_value = f(x, y)
        current_beepers += return_value[0]
        update(possible_list, return_value[1])
    see_north()
    robot.turn_left()
    robot.turn_left()
    robot.turn_left()
    if robot.front_is_clear() and check(x+1, y):
        robot.move()
        return_value = f(x, y)
        current_beepers += return_value[0]
        update(possible_list, return_value[1])
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
    return [current_beepers, possible_list]


possible_positions = []
for start_x in range(0, avenues):
    for start_y in range(0, streets):
        if visited[start_x][start_y]:
            continue
        robot = Robot(avenue=start_x+1, street=start_y+1)
        robot.set_trace('blue')
        return_values = f(start_x, start_y)
        if ans < return_values[0]:
            ans = return_values[0]
            possible_positions_temp = return_values[1]
            possible_positions.clear()
            for i in possible_positions_temp:
                a, b = i
                possible_positions.append((a+1, b+1))
print(possible_positions)
print(ans)
