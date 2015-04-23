__author__ = 'Naiii'

import time

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def multiple(n):
    for i in range(2, 21):
        # print(i)
        if not(n % i == 0):
            return False
    return True

def fast_multiple(n):
    tocheck = [11,13,14,16,17,18,19,20]
    for i in tocheck:
        if(not (n%i == 0)):
            return False
    return True

n = 2520
start = time.time()
while not multiple(n):
    # print(n)
    n += 2520
end = time.time()
print(n)
print("Time elapsed: " + str((end-start)*1000) + "[ms]")

n = 2520
start = time.time()
while not fast_multiple(n):
    # print(n)
    n += 2520
end = time.time()

print(n)
print("Time elapsed: " + str((end-start)*1000) + "[ms]")