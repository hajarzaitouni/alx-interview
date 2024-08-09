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
    """ Define the winner of the game """
    if x < 1 or not nums:
        return None
    n = max(nums)
    primes = calculates_primes(n)
    prime_set = set(primes)

    score = {"Maria": 0, "Ben": 0}

    for n in nums:
        count = sum(1 for i in range(1, n + 1) if i in prime_set)

        if count % 2 == 0:
            score["Ben"] += 1
        else:
            score["Maria"] += 1

    if score["Maria"] > score["Ben"]:
        return "Maria"
    if score["Maria"] < score["Ben"]:
        return "Ben"
    return None
