import math
import tkinter as tk
import sys

w = 700
h = 700

root = tk.Tk()
root.geometry('{}x{}'.format(w, h))
root.title("Simple Solar System")
canvas = tk.Canvas(root, height=h, width=w, bg='black')
canvas.pack()
root.update()


class Planet:
    sun_mass = 1.989 * math.pow(10, 30)
    G = 6.67 * math.pow(10, -11)

    def __init__(self, name, mass, distance, radius, color, canvas):
        self.name = name
        self.mass = mass
        self.distance = distance
        self.radius = radius
        self.canvas = canvas
        self.color = color
        self.angular_velocity = -math.sqrt(self.gravitational_force() /
                                           (self.mass * self.distance))
        self.oval_id = self.draw_initial_planet()
        self.scaled_radius = self.radius_scaler(self.radius)
        self.scaled_distance = self.distance_scaler(self.distance)

    def distance_scaler(self, value):
        # [57.91, 4497.1] scaled to [0, self.canvas.winfo_width()/2]
        return (self.canvas.winfo_width() / 2 - 1) * (value - 1e10) / (
                2.27e11 - 1e10) + 1

    def radius_scaler(self, value):
        # [2439, 6051.8] scaled to [0, self.canvas.winfo_width()/2]
        return (16 * (value - 2439) / (6052 - 2439)) + 2

    def draw_initial_planet(self):
        screen_dim = self.canvas.winfo_width()
        scaled_distance = self.distance_scaler(self.distance)
        scaled_radius = self.radius_scaler(self.radius)
        y = screen_dim / 2
        x = screen_dim / 2 + scaled_distance
        oval_id = self.canvas.create_oval(
            x - scaled_radius,
            y - scaled_radius,
            x + scaled_radius,
            y + scaled_radius,
            fill=self.color,
            outline=self.color)
        return oval_id

    def gravitational_force(self):
        f = self.G * (self.mass * self.sun_mass) / math.pow(self.distance, 2)
        return f

    def angular_position(self, t):
        theta = (0 + self.angular_velocity * t)
        return theta

    def coordinates(self, theta):
        screen_dim = self.canvas.winfo_width()
        y = self.scaled_distance * math.sin(theta) + screen_dim / 2
        x = self.scaled_distance * math.cos(theta) + screen_dim / 2
        return (x, y)

    def update_location(self, t):
        theta = self.angular_position(t)
        x, y = self.coordinates(theta)
        scaled_radius = self.scaled_radius
        self.canvas.create_rectangle(x, y, x, y, outline="grey")
        self.canvas.coords(self.oval_id, x - scaled_radius, y - scaled_radius, x + scaled_radius, y + scaled_radius)


# Todo
# ?????? Moon Class??? ?????? ???????????? ?????? ???????????? ?????? ????????? ???????????? ????????? ????????? ???.
class Moon(Planet):
    earth_mass = 5.973 * math.pow(10, 24)

    def __init__(self, name, mass, distance, radius, color, canvas, earth):
        super().__init__(name, mass, distance, radius, color, canvas)
        self.earth = earth
        self.oval_id = self.draw_moon()

        self.angular_velocity = -math.sqrt(self.gravitational_force() /
                                           (self.mass * self.distance))
        self.scaled_radius = self.radius_scaler(self.radius)
        self.scaled_distance = self.distance_scaler(self.distance)

    def draw_moon(self):
        screen_dim = self.canvas.winfo_width()
        y = screen_dim / 2
        x = screen_dim / 2 + self.earth.scaled_distance + self.radius
        oval_id = self.canvas.create_oval(
            x - self.radius,
            y - self.radius,
            x + self.radius,
            y + self.radius,
            fill=self.color, outline=self.color)
        return oval_id

    def gravitational_force(self):
        f = self.G * (self.mass * self.earth_mass) / math.pow(self.distance, 2)
        return f

    def coordinates(self, t):
        theta = super().angular_position(t)
        pos = self.canvas.coords(self.earth.oval_id)
        X = (pos[1]+pos[3])/2
        Y = (pos[0]+pos[2])/2
        y = self.scaled_distance * math.sin(theta) + X
        x = self.scaled_distance * math.cos(theta) + Y
        return (x, y)

    def update_location(self, t):
        x, y = self.coordinates(t)
        self.canvas.create_rectangle(x, y, x, y, outline="grey")
        self.canvas.coords(self.oval_id, x - self.scaled_radius, y - self.scaled_radius,
                           x + self.scaled_radius, y + self.scaled_radius)


# name,mass,distance,radius, color, canvas
mercury = Planet("Mercury", 3.302e23, 5.7e10, 2439.7, 'red2', canvas)
venus = Planet("Venus", 4.8685e24, 1.08e11, 6051.8, 'CadetBlue1', canvas)
earth = Planet("Earth", 5.973e24, 1.49e11, 6378, 'RoyalBlue1', canvas)
mars = Planet("Mars", 6.4185e23, 2.27e11, 3396, 'tomato2', canvas)
planets = [mercury, venus, earth, mars]
moon = Moon("Moon", 7.347e22, 3.844e8, 173, 'white', canvas, earth)

time = 0
time_step = 100000


def update_bodies_position():
    global time, time_step
    for planet in planets:
        planet.update_location(time)

    moon.update_location(time)

    time = time + time_step
    root.after(100, update_bodies_position)


update_bodies_position()

root.mainloop()
sys.exit()