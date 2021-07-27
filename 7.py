################################################################################
# Project Euler Problem 7
# 10001st prime
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
################################################################################

def nth_prime(n):
    primes = []
    i = 0
    while (len(primes) <= n) or (not primes):
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes[n - 1]


def is_prime(n):
    if n > 1:
        for i in range(2, int(n / 2) + 1):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False


def sieve(n):
    are_prime = [True for i in range(2, n + 1)]
    divisor = 2
    while divisor ** 2 <= n:
        if are_prime[divisor]:
            for i in range(divisor * 2, n + 1, divisor):
                are_prime[i - 2] = False
        divisor += 1
    primes = []
    for i in range(len(are_prime)):
        if are_prime[i]:
            primes.append(i + 2)
    return primes


print(nth_prime(10001))
