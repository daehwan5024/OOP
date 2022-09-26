import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import *

g = 9.8  # 중력 가속도
b = 2  # 저항 계수
m = 10  # 질량
theta = np.radians(45)  # 초기 각도
length = 1  # 줄 길이


def dU_dx(U, x):  # 미분 방정식
    return [U[1], -g / length * np.sin(U[0]) - b / m * U[1]]


U0 = [theta, 0]  # 초기값
xs = np.arange(0, 10, 0.05)  # 시간 값
Us = odeint(dU_dx, U0, xs)  # 미분 방정식 해결
ys = Us[:, 0]  # 필요한 값만 인덱싱
fig, ax = plt.subplots()  # 그림 보여주기
ax.set(xlim=[-length - 0.5, length + 0.5], ylim=[-length - 0.5, length + 0.5])  # 축 범위 설정
ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle='--')
line, = ax.plot([], [], color='b', linewidth=2)
obj, = ax.plot([], [], 'bo')
time_text = ax.text(-length - 0.2, -length - 0.2, '')


def init():  # 애니메이션 초기 함수
    line.set_data([], [])
    return line,


def iterr(i):  # 애니메이션 만들기
    theta = ys[i]
    x = length * np.sin(theta)
    y = -length * np.cos(theta)
    line.set_data([0, x], [0, y])
    obj.set_data([x], [y])
    time_text.set_text('time = {:.1f}'.format(xs[i]))
    return line, obj, time_text


anim = animation.FuncAnimation(fig, iterr, init_func=init, frames=len(ys), interval=0.05 * 1000, blit=True)  #pyplot으로 애니매이션 설정
anim.save('hw_17_20010_권대환.gif', fps=45)  # 동영상 저장
plt.show()  # 보여주기
