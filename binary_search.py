import random
import time

def naive_search(l, target):
    # example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    
    return -1


def binary_search(l, target, low = None, high = None):