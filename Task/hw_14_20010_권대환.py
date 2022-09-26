import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
direction = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def get(array, x, y, k):
    x += direction[k][0]
    y += direction[k][1]
    if x < 0:
        x += 50
    if x >= 50:
        x -= 50
    if y < 0:
        y += 50
    if y >= 50:
        y -= 50
    return array[x][y] == 1


def gol_step():
    current = np.zeros((50, 50))
    current[1, 2] = current[2, 3] = current[3, 3] = current[3, 2] = current[3, 1] = 1
    while True:
        next_step = np.zeros_like(current)
        for i in range(50):
            for j in range(50):
                alive = 0
                for k in range(8):
                    if get(current, i, j, k):
                        alive += 1
                if alive == 3 and current[i, j] == 0:
                    next_step[i, j] = 1
                elif 2 <= alive <= 3 and current[i, j] == 1:
                    next_step[i, j] = 1
        current = next_step
        yield current


arr = np.zeros((50, 50))
arr[1, 2] = arr[2, 3] = arr[3, 3] = arr[3, 2] = arr[3, 1] = 1
fig = plt.figure()

im = plt.imshow(arr, cmap='gray')
temp = gol_step()


def animate_func(i):
    next_arr = next(temp)
    im.set_array(next_arr)
    return im


anim = animation.FuncAnimation(fig, animate_func, interval=20, repeat=False)
plt.show()
