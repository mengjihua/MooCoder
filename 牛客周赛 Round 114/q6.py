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

t = 1

def judge(x):
    s = str(x)
    vis = set()
    pre = ''
    for ch in s:
        if ch not in '123':
            return False
        if ch == pre:
            return False
        vis.add(ch)
        pre = ch
    return len(vis) == 3

def solve():
    n = int(input())
    
    mn, mx = 10 ** (n - 1), 10 ** n - 1
    for i in range(mn, mx + 1):
        for j in range(mn, i + 1):
            if judge(i * j):
                return f'{i} {j}'
    
    return -1

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep="\n")