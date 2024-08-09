#!/usr/bin/python3
""" Prime Game """


def is_prime(num):
    """ Checks if a number is prime or not """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def calculates_primes(max_num):
    """ Calculates the prime numbers up to max_num """
    primes = []
    for i in range(max_num + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def isWinner(x, nums):
    """ Prime Game """
    if x < 1 or not nums:
        return None
    n = max(nums)
    primes = calculates_primes(n)
    prime_count = [0] * (n + 1)
    count = 0
    for i in range(1, n + 1):
        if i in primes:
            count += 1
        prime_count[i] = count
    winner = 0
    for n in nums:
        winner += prime_count[n] % 2 == 1
    if winner * 2 == len(nums):
        return None
    if winner * 2 == 0:
        return None
    if winner * 2 == len(nums):
        return None
    if winner > len(nums) - winner:
        return "Maria"
    return "Ben"
