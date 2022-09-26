from cs1robots import *
import random
load_world('input_files/finalMaze2.wld')
orient_dict = {0:'N', 1: 'E', 2: 'S', 3: 'W'}
initial_orient = random.randint(0, 3)
gshs1 = Robot(color="light_blue", orientation=orient_dict[initial_orient], avenue=11, street=11)
gshs1.set_trace(color='blue')


def turn_right(robot):
    for i in range(3):
        robot.turn_left()


def turn_around(robot):
    for i in range(2):
        robot.turn_left()


command_list: str
with open("input_files/command2.txt", "r") as f:
    command_list = f.read()


def is_circular(x, y, path, robot):
    print("Path len: ", len(path))
    for movement in path:
        if movement == 'M':
            if robot.front_is_clear():
                robot.move()
            else:
                turn_around(robot)
                robot.move()
        elif movement == 'L':
            robot.turn_left()
        elif movement == 'R':
            turn_right(robot)
    if robot.get_pos() == (x, y):
        return True
    return False


print(is_circular(11, 11, command_list, gshs1))
