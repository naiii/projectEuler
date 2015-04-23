__author__ = 'Naiii'

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(n):
    number = str(n)
    rebmun = number[::-1]  # StackOverflow HYPE
    if number == rebmun:
        return True
    else:
        return False


# for i in range(10, 100):
#     for y in range(10, 100):
#         if is_palindrome(i*y):
#             print(str(i) + " * " + str(y) + " = " + str(i*y))
res = 0
for i in range(100, 1000):
    for y in range(100, 1000):
        if is_palindrome(i*y):
            if i*y > res:
                res = i*y

print(res)