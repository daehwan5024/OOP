import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]


def gol_step():
    current = np.zeros([50, 50])
    current[1, 2] = current[2, 3] = current[3, 3] = current[3, 2] = current[3, 1] = 1
    while True:
        answer = np.zeros([50, 50])
        for i in range(50):
            for j in range(50):
                nl = 0
                for k in range(8):
                    if current[(i + dx[k] + 4) % 4, (j + dy[k] + 4) % 4] == 1:
                        nl += 1
                if current[i, j] == 0:
                    if nl == 3:
                        answer[i, j] = 1
                elif nl == 1 or nl == 4:
                    answer[i, j] = 0
        current = answer
        yield answer


arr = np.zeros([50, 50])
arr[1, 2] = arr[2, 3] = arr[3, 3] = arr[3, 2] = arr[3, 1] = 1
Next = gol_step()
fig = plt.figure(figsize=(5, 5))
im = plt.imshow(arr, cmap='gray')

def animattte(i):
    next_arr = next(Next)
    im.set_array(next_arr)
    return im


anim = animation.FuncAnimation(fig, animattte, blit=False, interval=10, repeat=False)
plt.show()
