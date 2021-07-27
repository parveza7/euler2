###############################################################################
# Project Euler Problem 3
# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
###############################################################################

# Code that takes a few years to finish and possibly might not work
# def largest_prime_factor(n):
#    largest = 0
#    for i in range(int(n * 1/2) + 1):
#        if i <= 1:
#            continue
#        if is_prime(i) and (n % i == 0):
#            largest = max(largest, i)
#        if i % 1000 == 0:
#            print(f"Checked number {i}")
#    if largest == 0:
#        largest = n
#    return largest

# Extremely similar code that takes slightly less years to finish and also possibly might not work
# def largest_prime_factor(n):
#     largest = 0
#     for i in range(int(n * 1/2) + 1, 2, -1):
#         if is_prime(i) and (n % i == 0):
#             largest = i
#             break
#         if i % 1000 == 0:
#             print(f"Checked number {i}")
#     if largest == 0:
#         largest = n
#     return largest


# Start with a trial divisor of 2; 13195 divided by 2 leaves a remainder of 1, so 2 does not divide 13195, and
# we can go on to the next trial divisor. Next we try 3, but that leaves a remainder of 1; then we try 4, but
# that leaves a remainder of 3. The next trial divisor is 5, and that does divide 13195, so we output 5 as a factor of 13195,
# reduce the original number to 2639 = 13195 / 5, and try 5 again. Now 2639 divided by 5 leaves a remainder of 4, so we advance to 6,
# which leaves a remainder of 5, then we advance to 7, which does divide 2639, so we output 7 as a factor of 2639
# (and also a factor of 13195) and reduce the original number again to 377 = 2639 / 7. Now we try 7 again, but it fails to divide 377,
# as does 8, and 9, and 10, and 11, and 12, but 13 divides 2639. So we output 13 as a divisor of 377 (and of 2639 and 13195) and
# reduce the original number again to 29 = 377 / 13. As this point we are finished, because the square of the trial divisor,
# which is still 13, is greater than the remaining number, 29, which proves that 29 is prime; that is so because if n=pq, then
# either p or q must be less than, or equal to the square root of n, and since we have tried all those divisors,
# the remaining number, 29, must be prime. Thus, 13195 = 5 * 7 * 13 * 29.


def largest_prime_factor(n):
    largest = n + 0
    i = 1
    while i * i <= largest:
        if is_prime(i) and (largest % i == 0):
            largest = largest // i
        else:
            i = i + 1
    return largest


def is_prime(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False


print(largest_prime_factor(600851475143))
