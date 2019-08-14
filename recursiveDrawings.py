#Turtle draws a spiral depending on initialLength, angle, and multiplier

import turtle

def spiral(initialLength, angle, multiplier):
    '''draws a spiral using a turtle and recursion'''
    if initialLength < 1 and multiplier < 1:
        return
    if initialLength > 200 and multiplier > 1:
        return

    turtle.forward(initialLength)
    turtle.right(angle)

    spiral(initialLength * multiplier, angle, multiplier)

#Test case
spiral(1, -45, 1.1)

