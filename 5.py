###############################################################################
# Project Euler Problem 3
# Smallest multiple
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
###############################################################################

def smallest_divisible_by(n):
    factorization = []
    factorizations = [prime_factors(i) for i in range(n)]
    for i in range(n):
        if factorization == []:
            factorization = factorizations[i]
        else:
            union = []
            [union.extend([n] * max(factorization.count(n), factorizations[i].count(n))) for n in range(min(
                min(factorization), min(factorizations[i])), max(max(factorization), max(factorizations[i]))+1)]
            factorization = union
    total = 1
    for i in factorization:
        total *= i
    return total


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


print(smallest_divisible_by(20))
