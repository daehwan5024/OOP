import random
import cs1robots as cs
n = 20
trials = 30
deadEnds = 0


def move_robot(x_pos: int, y_pos: int, direction: int):
    if direction == 1:
        x_pos += 1
    elif direction == 2:
        x_pos -= 1
    elif direction == 3:
        y_pos += 1
    else:
        y_pos -= 1
    return x_pos, y_pos


def possible(x_pos: int, y_pos: int, direction: int, visited_places):
    x_pos, y_pos = move_robot(x_pos, y_pos, direction)
    if not(0 < x_pos <= n and 0 < y_pos <= n):
        return False
    else:
        return not(visited_places[x_pos-1][y_pos-1])


class Robot(cs.Robot):
    def see_north(self):
        while not self.facing_north():
            self.turn_left()

    def turn_right(self):
        self.turn_left()
        self.turn_left()
        self.turn_left()

    def turn_around(self):
        self.turn_left()
        self.turn_left()

    def movement(self, direction):
        self.drop_beeper()
        if direction == 1:
            self.turn_right()
            self.move()
            self.see_north()
        elif direction == 2:
            self.turn_left()
            self.move()
            self.see_north()
        elif direction == 3:
            self.move()
        elif direction == 4:
            self.turn_around()
            self.move()
            self.see_north()

    def go_home(self):
        goal_x, goal_y = 1, 1
        current_x, current_y = self.get_pos()
        for _ in range(current_y - goal_y):
            self.turn_around()
            self.move()
            self.turn_around()
        for _ in range(current_x - goal_x):
            self.turn_left()
            self.move()
            self.turn_right()
        self.see_north()

    def go_middle(self):
        self.see_north()
        self.turn_right()
        for _ in range(9):
            self.move()
        self.turn_left()
        for _ in range(9):
            self.move()


cs.create_world(n, n)
gshs = Robot(beepers=n*n*trials)
gshs.set_trace('blue')
way = [1, 2, 3, 4]
for t in range(trials):
    visited = [[False for _ in range(0, n)] for _ in range(0, n)]
    x = n//2
    y = n//2
    gshs.go_middle()
    while True:
        if (x == 1) or (x == n) or (y == 1) or (y == n):
            gshs.drop_beeper()
            gshs.go_home()
            break
        visited[x-1][y-1] = True
        random.shuffle(way)
        if possible(x, y, way[0], visited):
            gshs.movement(way[0])
            x, y = move_robot(x, y, way[0])
        elif possible(x, y, way[1], visited):
            gshs.movement(way[1])
            x, y = move_robot(x, y, way[1])
        elif possible(x, y, way[2], visited):
            gshs.movement(way[2])
            x, y = move_robot(x, y, way[2])
        elif possible(x, y, way[3], visited):
            gshs.movement(way[3])
            x, y = move_robot(x, y, way[3])
        else:
            gshs.drop_beeper()
            deadEnds += 1
            break
    gshs.go_home()
    gshs.clear_beeper_trace()
    gshs.set_trace('blue')
print(str(100*deadEnds//trials) + '% dead ends')
