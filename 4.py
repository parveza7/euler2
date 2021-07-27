###############################################################################
# Project Euler Problem 4
# Largest palindrome product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
###############################################################################

def largest_palindrome(digits):
    largest = 0
    for i in range((10 ** digits) - 1, (10 ** (digits - 1)) - 1, -1):
        for j in range((10 ** digits) - 1, (10 ** (digits - 1)) - 1, -1):
            if str(i * j)[::-1] == str(i * j):
                largest = max(i * j, largest)
    return largest

print(largest_palindrome(3))
