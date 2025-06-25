from turtle import *

screen = Screen()
screen.title("Etch A Sketch by i9mm")
screen.bgcolor("white")

pen = Turtle()
pen.pensize(3)
pen.speed(0)

def move_forward():
    pen.forward(20)

def move_backward():
    pen.backward(20)

def turn_left():
    pen.left(15)

def turn_right():
    pen.right(15)

def clear_drawing():
    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")   
screen.onkey(clear_drawing, "c")

screen.mainloop()
