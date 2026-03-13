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
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    d = [b[i] - a[i] for i in range(n)]
    
    cycle = 0
    mx = 0
    for i in range(n):
        mx = fmax(mx, a[i] - cycle)
        cycle += d[i]
        
    if cycle >= 0:
        if x >= mx:
            return 'Infinity'
        else:
            cnt = 0
            for i in range(n):
                if x >= a[i]:
                    x += d[i]
                    cnt += 1
                else:
                    break
            return str(cnt)
    else:
        if x < mx:
            cnt = 0
            for i in range(n):
                if x >= a[i]:
                    x += d[i]
                    cnt += 1
                else:
                    break
            return str(cnt)
        else:
            k = (x - mx) // (-cycle) + 1
            x += k * cycle
            idx = 0
            for i in range(n):
                if x >= a[i]:
                    x += d[i]
                    idx += 1
                else:
                    break
            return str(k * n + idx)

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep="\n")


# 1
# 1 3
# 2
# 1