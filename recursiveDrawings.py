#Turtle draws a spiral depending on initialLength, angle, and multiplier
#Also draws a tree. A very nice tree
#Emily and Jennifer

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
    """Draws a recursive tree based off how long you want it to be and how many times you want it to repeat"""
    if height == 1:
        turtle.forward(trunkLength)
        turtle.right(45)
        turtle.forward(trunkLength // 2)
        turtle.backward(trunkLength // 2)
        turtle.left(90)
        turtle.forward(trunkLength // 2)
        turtle.backward(trunkLength // 2)
        turtle.right(45)
    
    #Recurses on tree branch
    else:
        #turtle moves forward and right
        turtle.forward(trunkLength)
        turtle.right(45)
        tree(trunkLength//2, height-1)
        #Return of the turtle and then it turns left
        turtle.backward(trunkLength // 2)
        turtle.left(90)
        tree(trunkLength//2, height-1)
        #Return of the Turtle 2: Uprising
        turtle.backward(trunkLength // 2)
        turtle.right(45)
#Test case
#spiral(1, -45, 1.1)
turtle.speed(1)
turtle.left(90)
tree(200, 4)

