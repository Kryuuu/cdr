from turtle import *
from random import *
from time import sleep

colormode(255)
speed(0)
shape("turtle")
hideturtle()

def randomcolour():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color(red, green, blue)

def randomplace():
    penup()
    x = randint(-100, 100)
    y = randint(-100, 100)
    goto(x, y)
    pendown()

def randomheading():
    number = randint(1, 360)
    setheading(number)

def drawrectangle():
    randomcolour()
    randomplace()
    hideturtle()
    length = randint(10, 100)
    height = randint(10, 100)
    begin_fill()
    forward(length)
    right(90)
    forward(height)
    right(90)
    forward(length)
    right(90)
    forward(height)
    right(90)
    end_fill()

def drawcircle():
    randomcolour()
    randomplace()
    radius = randint(10, 130)
    dot(radius)

def drawstar():
    randomcolour()
    randomplace()
    randomheading()
    begin_fill()
    size = randint(10, 50)
    for side in range(5):
        forward(size)
        right(144)
    end_fill()

clear()
setheading(0)

jumlah_lingkaran = randint(60, 70)

try:
    tracer(0)
    for i in range(jumlah_lingkaran):
        drawcircle()
        update()
        sleep(0.03)
    done()
except (Terminator, Exception):
    pass
