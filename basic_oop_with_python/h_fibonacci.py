'''
A function fibonacci(x) that computes the fibonacci number of the parameter.
'''
import math
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    elif n == 2:
        return 1
    elif n < 0:
        if n == -1:
            return 1
        elif n == -2:
            return -1
        elif n < -2:
            return (fibonacci(n+2) - fibonacci(n+1))
    elif n > 2:
        return (fibonacci(n-1) + fibonacci(n-2))
