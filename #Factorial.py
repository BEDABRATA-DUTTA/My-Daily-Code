#Factorial
#first method using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))    

#second method using math module
import math
print(math.factorial(5))
    