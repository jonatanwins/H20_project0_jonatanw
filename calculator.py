def add(x,y):
    return x+y

def factorial(x):
    if x != 0:
        return x*factorial(x-1)
    else:
        return 1

def sin(x,N):
    sum = 0
    for n in range(0,N+1):
        sum += (((-1)**n)*x**(2*n+1))/factorial(2*n+1)
    return sum

def divide(x,y):
    return x/y

def double_factorial(x):
    if x > 1:
        return x*double_factorial(x-2)
    else:
        return 1

def absolute_value(x):
    if x < 0:
        x = -x
    return x