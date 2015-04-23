__author__ = 'Naiii'

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

a = []

for i in range(0, 1000, 3):
    a.append(i)

for i in range(0, 1000, 5):
    a.append(i)

a = list(set(a))  # take out all doubles
b = sum(a)
print(b)