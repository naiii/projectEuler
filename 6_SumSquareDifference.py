__author__ = 'Naiii'


"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

max = 100
sumOfSquares = 0
for x in range(0, max + 1):
    sumOfSquares += x**2

print(sumOfSquares)

squareOfSome = 0
for x in range(0, max + 1):
    squareOfSome += x

squareOfSome **= 2

print(squareOfSome)

print(squareOfSome-sumOfSquares)