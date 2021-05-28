import random
import time

def naive_search(l, target):
    # example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    
    return -1


def binary_search(l, target, low = None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) -1
    
    if high < low:
        return -1

    # example l = [1, 3, 5, 10, 12]     should return 3
    midpoint = (low + high) // 2    # 2
