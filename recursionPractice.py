#Emily and Jennifer
# returns the product of two integers
def recProduct(a,b):
    """Takes in two integers as parameters. Returns the product of said integers using addition and recursion"""
    if b == 0 or a ==0:
        return 0
    else:
        if (a>0 and b>0) or (a<0 and b>0):
            return recProduct(a, b-1) + a
        elif (a>0 and b<0) or (a<0 and b<0):
            return recProduct(a, b+1) -a

#Testcases
print(recProduct(0,5))
print(recProduct(1,5))
print(recProduct(-1,5))
print(recProduct(5,-1))
print(recProduct(-5,-1))
