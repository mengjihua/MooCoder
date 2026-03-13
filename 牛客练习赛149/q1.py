from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sys import setrecursionlimit, stdin, stdout
from random import getrandbits
setrecursionlimit(5 * 10 ** 4 + 1)
input = lambda: stdin.readline().rstrip()
RD = getrandbits(31)
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)

t = int(input())

def solve():
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    
    res = 0
    for i in range(1, n):
        if lst[i] <= lst[i - 1]:
            temp = lst[i - 1] + 1
            res += temp - lst[i]
            lst[i] = temp
    return res
    

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep="\n")