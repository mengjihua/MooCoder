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
    s = input().strip()
    
    cnt = Counter(s)
    
    if not ('1' in cnt and '2' in cnt and '3' in cnt):
        return -1
    
    res = inf
    
    for i in range(n - 2):
        sub = s[i:i + 3]
        sub_cnt = Counter(sub)
        
        cur = 0
        if sub_cnt['1'] > 0:
            cur += 1
        if sub_cnt['2'] > 0:
            cur += 1
        if sub_cnt['3'] > 0:
            cur += 1
        
        temp = 3 - cur
        res = fmin(res, temp)
    
    return res if res != inf else -1

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep="\n")