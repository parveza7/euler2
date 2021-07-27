################################################################################
# Project Euler Problem 10
# Summation of primes
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
################################################################################

def sum_primes_lower_than(n):
    are_prime = [True for i in range(2, n + 1)]
    divisor = 2
    while divisor ** 2 <= n:
        if are_prime[divisor - 2]:
            for i in range(divisor * 2, n + 1, divisor):
                are_prime[i - 2] = False
        divisor += 1
    primes = []
    for i in range(len(are_prime)):
        if are_prime[i]:
            primes.append(i + 2)
    return sum(primes)


print(sum_primes_lower_than(2000000))
