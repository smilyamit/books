'''This is just for testing purposes'''
#First Program

# Make an efficient prime number program using the isqrt function
import math
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.isqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

for num in range(2, 101):
    if is_prime(num):
        print(num)
