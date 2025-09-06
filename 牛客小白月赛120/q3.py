from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sys import setrecursionlimit, stdin, stdout
from random import getrandbits
setrecursionlimit(5 * 10 ** 4 + 1)
input = lambda: stdin.readline().rstrip()
RD = getrandbits(31)
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b

t = int(input())

def solve():
    n = int(input())
    if n == 1:
        return [1]
    if n == 2:
        return [-1]
    res = list(range(1, n + 1))
    if n % 2 == 0:
        res[1], res[2] = res[2], res[1]
    return res

ans = []
for _ in range(t):
    ans.append(solve())

# print(ans)
for i in ans:
    print(*i)