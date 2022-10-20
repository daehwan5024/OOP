import random
n = 20
trials = 1000
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


way = [1, 2, 3, 4]
for t in range(trials):
    visited = [[False for _ in range(0, n)] for _ in range(0, n)]
    x = n//2
    y = n//2
    while True:
        if (x == 1) or (x == n) or (y == 1) or (y == n):
            break
        visited[x-1][y-1] = True
        random.shuffle(way)
        if possible(x, y, way[0], visited):
            x, y = move_robot(x, y, way[0])
        elif possible(x, y, way[1], visited):
            x, y = move_robot(x, y, way[1])
        elif possible(x, y, way[2], visited):
            x, y = move_robot(x, y, way[2])
        elif possible(x, y, way[3], visited):
            x, y = move_robot(x, y, way[3])
        else:
            deadEnds += 1
            break
print(str(100*deadEnds//trials) + '% dead ends')
