import math
import random

def fib(n):
    Phi=(1+math.sqrt(5))/2
    phi=(1-math.sqrt(5))/2
    return int((Phi**n-phi**n)/math.sqrt(5))

for i in range(1,10):
    print fib(i)+5

print random.choice([True,False])
