from swampy.TurtleWorld import *
import math


def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t,angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)


    

def circle(t, r):
   arc(t, r, 360)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length/3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)
    


def pedel(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180 - angle)

def move_pen(t, dis):
    pu(t)
    fd(t,dis)
    pd(t)


def flower(t, r, n, angle):
    for i in range(n):
        pedel(t,r, angle)
        lt(t, 360.0 / n)

def polygon_wheel(t, n, length):
    inner_length = (length / 2) / math.sin(math.pi / n)
    angle = (n - 2) * 180 / n
    for i in range(n):
        fd(t, length)
        lt(t, 180 - angle/2)
        fd(t, inner_length)
        move_pen(t, -inner_length)
        rt(t, angle/2)


    
world = TurtleWorld()
t = Turtle()
t.delay = 0.00001

print t

move_pen(t,-100)
flower(t, 60, 7, 60)
move_pen(t, 150)
flower(t, 40, 10, 80)
move_pen(t, 150)
flower(t, 140, 20, 20)

move_pen(t,150)
lt(t, 20)
polygon_wheel(t, 5, 80)

rt(t, 20)
move_pen(t, 200)
polygon_wheel(t, 6, 80)

rt(t, 30)
lt(t, 15)
move_pen(t, 200)
polygon_wheel(t, 7, 80)


die(t)

wait_for_user()


