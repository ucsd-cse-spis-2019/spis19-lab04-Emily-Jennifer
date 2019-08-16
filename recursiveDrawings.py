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

def snowflakeSide(sidelength, levels):
    '''Draws one side of a snowflake recursively depending on sidelength and levels'''
    #base case - draw one line segment
    if levels == 0:
        turtle.forward(sidelength)
    #recurse four times for snowflake side 
    else:
        snowflakeSide(sidelength//3, levels-1)
        turtle.left(60)
        snowflakeSide(sidelength//3, levels-1)
        turtle.right(120)
        snowflakeSide(sidelength//3, levels-1)
        turtle.left(60)
        snowflakeSide(sidelength//3, levels-1)
    
    
def snowflake(sidelength, levels):
    '''Calls snowflakeSide three times to draw triangle'''

    snowflakeSide(sidelength,levels)
    turtle.right(120)
    snowflakeSide(sidelength,levels)
    turtle.right(120)
    snowflakeSide(sidelength,levels)



turtle.speed(0)        

#Test case tree
#spiral(1, -45, 1.1)
#turtle.left(90)
#tree(200, 4)

#Test case snowflake
#snowflakeSide(100, 2)
snowflake(100, 4)







