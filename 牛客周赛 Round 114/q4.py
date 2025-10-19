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

MOD = 998244353

t = 1

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 1:
        return a[0]
    if n == 2:
        return fmax(a[0], a[1])
    
    dp = [0] * n
    dp[0] = a[0]
    dp[1] = fmax(a[0], a[1])
    
    for i in range(2, n):
        dp[i] = fmax(dp[i - 1], dp[i - 2] + a[i])
    
    return dp[n - 1]
    

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep="\n")