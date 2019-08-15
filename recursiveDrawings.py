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


def tree(trunkLength, height):
    if height == 1:
        turtle.forward(trunkLength)
        turtle.right(45)
        turtle.forward(trunkLength // 2)
        turtle.backward(trunkLength // 2)
        turtle.left(90)
        turtle.forward(trunkLength // 2)
        turtle.backward(trunkLength // 2)
        turtle.right(45)
        #turtle.backward(trunkLength)

    else:
        turtle.forward(trunkLength)
        turtle.right(45)
        #turtle.forward(trunkLength // 2)
        tree(trunkLength//2, height-1)
        turtle.backward(trunkLength // 2)
        turtle.left(90)
        #turtle.forward(trunkLength // 2)
        tree(trunkLength//2, height-1)
        turtle.backward(trunkLength // 2)
        turtle.right(45)
        #turtle.backward(trunkLength)
        #turtle.forward(trunkLength)
        #turtle.right(45)
        #print("turtle moving right!" + str(turtle.heading()))
        #tree(trunkLength * .5, height-1)
        #print("Turtle going back!" + str(turtle.heading()))
        #turtle.left(45)
        #turtle.backward(trunkLength)
        #turtle.left(90)
        #print("turtle moving lef!" + str(turtle.heading()))
        #t2ree(trunkLength*.5, height-1)
        #print("Turtle going back 2.0!" + str(turtle.heading()))
        #turtle.right(135)
        #turtle.backward(trunkLength)
        #turtle.right(45)
        input("hi")
#Test case
#spiral(1, -45, 1.1)
turtle.speed(1)
turtle.left(90)
tree(200, 4)

