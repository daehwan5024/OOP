import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
direction = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
gshs = np.array([
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
     [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
     [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
])

def get(array, x, y, k):
    x += direction[k][0]
    y += direction[k][1]
    if x < 0:
        x += 60
    if x >= 60:
        x -= 60
    if y < 0:
        y += 60
    if y >= 60:
        y -= 60
    return array[x][y] == 1


def gol_step():
    current = np.zeros((60, 60))
    current[1:10, 1:37] = gshs
    while True:
        next_step = np.zeros_like(current)
        for i in range(60):
            for j in range(60):
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


arr = np.zeros((60, 60))
arr[1:10, 1:37] = gshs
fig = plt.figure(figsize=(7, 7))

im = plt.imshow(arr, cmap='gray')
temp = gol_step()


def animate_func(i):
    next_arr = next(temp)
    im.set_array(next_arr)
    return [im]


anim = animation.FuncAnimation(fig, animate_func, blit=False, interval=10, frames=1000, repeat=False)
#anim.save('test.gif', fps=60)
plt.show()
