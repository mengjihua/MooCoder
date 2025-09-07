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

# def solve():
#     n = int(input())
#     a = list(map(int, input().split()))
#     odd = [x for x in a if x & 1]
#     even = [x for x in a if not x & 1]
#     odd.sort()
#     even.sort()
#     return even + odd

def solve():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    return sorted(a, key=lambda x: (x & 1, not x & 1))

ans = []
for _ in range(t):
    ans.append(solve())
for i in ans:
    print(*i)