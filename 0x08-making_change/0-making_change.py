#!/usr/bin/python3
""" Making Change """


def makeChange(coins, total):
    """ Make Change function """
    if total <= 0:
        return 0
    coins.sort()
    coins.reverse()
    len_coins = len(coins)
    i = 0
    change = 0
    while i < len_coins and total > 0:
        if coins[i] <= total:
            total -= coins[i]
            change += 1
        else:
            i += 1
    if total != 0:
        return -1
    return change
