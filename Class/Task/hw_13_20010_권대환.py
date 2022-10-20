import numpy as np
direction = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def get(array, x, y, k):
    x += direction[k][0]
    y += direction[k][1]
    if x < 0:
        x += 4
    if x >= 4:
        x -= 4
    if y < 0:
        y += 4
    if y >= 4:
        y -= 4
    return array[x][y] == 1


def gol_step(arr):
    ans = np.zeros((4, 4))
    for i in range(4):
        for j in range(4):
            alive = 0
            for k in range(8):
                if get(arr, i, j, k):
                    alive += 1
            if alive == 3 and arr[i, j] == 0:
                ans[i, j] = 1
            elif 2 <= alive <= 3 and arr[i, j] == 1:
                ans[i, j] = 1
    return ans


current = np.array([1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]).reshape(4, 4)
next = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1]).reshape(4, 4)
print(gol_step(current))
print(np.sum(gol_step(current) - next))
