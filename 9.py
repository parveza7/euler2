################################################################################
# Project Euler Problem 9
# Special Pythagorean triplet
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
################################################################################

def pythagorean(n):
    for i in range(n):
        for j in range(n):
            a = abs((i ** 2) - (j ** 2))
            b = 2 * i * j
            c = (i ** 2) + (j ** 2)
            if a + b + c == n:
                return a * b * c


print(pythagorean(1000))
