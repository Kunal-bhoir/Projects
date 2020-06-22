def add(x,y):
    return x + y 

def sub(x,y):
    return x - y 

def multiply(x,y):
    return x * y

def Divide(x,y):
    if y == 0:
        raise ValueError('cannot ivide by zero')
    return x / y     

print(add(10,5))     
