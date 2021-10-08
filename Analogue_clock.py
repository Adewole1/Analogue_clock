import turtle
import math
from multiprocessing import Process
import _thread
from datetime import datetime

bob = turtle.Turtle()
grace = turtle.Turtle()
sec_hand = turtle.Turtle()
min_hand = turtle.Turtle()
hour_hand = turtle.Turtle()

bob.shape('circle')
grace.shape('classic')

bob.shapesize(0.5,0.5)
bob.pensize(2)

sec_hand.color('blue')
min_hand.color('green')
hour_hand.color('red')

bob.left(90)
grace.left(90)
bob.up()
grace.up()
bob.forward(100)
grace.forward(80)
bob.down()
grace.down()
bob.right(90)
grace.right(90)

grace.speed(0)
bob.speed(0)


def loop_a():
    len_circle = 2*math.pi*100
    length = 1
    count = 1
    while count <= 360 and length<=(len_circle):
        bob.forward((len_circle)/360)
        bob.right(1)
        count += 1
        length += (len_circle)/360
    bob.hideturtle()
        

def loop_c():
    length = 1
    count = 1
    len_circle = 2*math.pi*80
    while count <= 360 and length<=(len_circle):
        # print(grace.heading())
        grace.penup()
        if grace.heading() in range(0,361,30):
            # grace.pendown()
            grace.dot(5)
        elif grace.heading() in range(0,361,6):
            grace.dot(3)
        grace.forward((len_circle)/360)
        grace.right(1)
        count += 1
        length += (len_circle)/360
    grace.hideturtle()
        
        

def loop_b():
    sec_hand.dot(10,'blue')
    sec_hand.up()
    sec_hand.screen.addshape('line',((0,0), (70,0)))
    min_hand.screen.addshape('line2',((0,0), (80,0)))
    hour_hand.screen.addshape('line3',((0,0), (50,0)))
    sec_hand.shape('line')
    min_hand.shape('line2')
    hour_hand.shape('line3')
    while True:
        sekunde = datetime.now().second + datetime.now().microsecond*0.000001
        minutes = datetime.now().minute *60 + sekunde
        if datetime.now().hour > 12:
            hours = ((datetime.now().hour - 12)*5*60 + datetime.now().minute)*60 + sekunde
        else:
            hours = ((datetime.now().hour - 12)*5*60 + datetime.now().minute)*60 + sekunde
        sec_hand.setheading(180-(sekunde*6))
        min_hand.setheading(180-(minutes*0.1))
        hour_hand.setheading(180-(hours*(360/216000)))
        

# loop_a()
# loop_b()


if __name__ == '__main__':
    _thread.start_new_thread(loop_a, ())
    _thread.start_new_thread(loop_b, ())
    _thread.start_new_thread(loop_c, ())
    # _thread.start_new_thread(loop_d, ())


turtle.done()
