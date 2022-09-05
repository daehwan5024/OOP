from cs1robots import *
import random
load_world('../homework/finalMaze2.wld')
orient_dict = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}

initial_orient = random.randint(0, 3)
gshs1 = Robot(color="light_blue", orientation=orient_dict[initial_orient], avenue=11, street=11)
gshs1.set_trace(color='blue')
gshs1.set_pause(1)

initial_orient = random.randint(0, 3)
gshs2 = Robot(color="yellow", orientation=orient_dict[initial_orient], avenue=11, street=11)
gshs2.set_trace(color='blue')
gshs2.set_pause(1)


def turn_right(robot):
    for i in range(3):
        robot.turn_left()


def turn_around(robot):
    for i in range(2):
        robot.turn_left()


with open("../homework/command.txt", "r") as f:
    command1 = f.readline()
    command2 = f.readline()


def is_circular(x, y, path, robot):
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


print(is_circular(11, 11, command1, gshs1))
print(is_circular(11, 11, command2, gshs2))
