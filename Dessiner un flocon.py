from turtle import*
import random
shape("turtle")
speed(5)
pencolor("white")
pensize(4)
hideturtle
Screen().bgcolor("turquoise")
def formev():
    right(25)
    forward(50)
    backward(50)
    left(50)
    forward(50)
    backward(50)
    right(25)
def brancheFlocon():
    for x in range(0,4):
        forward(30)
        formev()
    backward(120)
def flocon():
    for x in range(0,18):
        brancheFlocon()
        right(80)
flocon()
