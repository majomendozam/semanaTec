"""Paint, for drawing shapes.
<<<<<<< HEAD
Ximena Gonzalez
=======

María José Mendoza Muñiz
06/05/2021
>>>>>>> 9dcd65e170e8bb4876c4720a494c1e25cbde4aa1
Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""

from turtle import *
from freegames import vector


pensize(8)
fillcolor("yellow")
pencolor("green")

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(8):
        forward(end.x - start.x)
        left(45)

    end_fill()


def rectangle(start, end):
    "Draw rectangle from start to end."


    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def triangle(start, end):
    "Draw triangle from start to end."
    pass  # TODO

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('red'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
<<<<<<< HEAD
onkey(lambda: color('black'), 'R')
=======
onkey(lambda: color('red'), 'R')
onkey(lambda: color('orange'), 'O')
>>>>>>> 9dcd65e170e8bb4876c4720a494c1e25cbde4aa1
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: color('cyan'), 'C')
onkey(lambda: color('orange'), 'O')
onkey(lambda: color('magenta'), 'M')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
