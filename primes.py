import math
"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    i = 2
    if number_of_primes < 0 or number_of_primes == 0:
        raise ValueError
    while len(list) < number_of_primes:
        if is_prime(i):
            list.append(i)
        i += 1
    return list

def is_prime(num):
    for i in range(2,num):
        if(num%i == 0):
            return False
    return True

