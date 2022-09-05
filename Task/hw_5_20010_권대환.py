from cs1robots import *
load_world('../worlds/foru.wld')
gshs = Robot(beepers=10000)
gshs.set_trace(color='blue')
prime = []
nth_prime = 0
prime_now = 2
nth_line = 0


def is_prime(temp: int):
    for _ in prime:
        if temp % _ == 0:
            return False
    prime.append(temp)
    return True


def up(temp: int):
    if temp % 2 == 0:
        gshs.turn_left()
        gshs.move()
        gshs.turn_left()
    else:
        gshs.turn_left()
        gshs.turn_left()
        gshs.turn_left()
        gshs.move()
        gshs.turn_left()
        gshs.turn_left()
        gshs.turn_left()


while nth_prime < 30:
    if is_prime(prime_now):
        for _ in range(0, prime_now):
            gshs.drop_beeper()
        prime_now += 1
        nth_prime += 1
        if gshs.front_is_clear():
            gshs.move()
        else:
            up(nth_line)
            nth_line += 1
    else:
        prime_now += 1
