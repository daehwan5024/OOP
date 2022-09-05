from cs1robots import *


def to_int(input_list):
    return int(input_list[0]), int(input_list[1])


load_world('worlds/myworld.wld')
f = open('input1.in')
avenue_robot, street_robot = to_int(f.readline().split(' '))
avenues, streets = to_int(f.readline().split(' '))
f.close()

robot = Robot(avenue=avenue_robot, street=street_robot)
robot.set_trace('blue')

