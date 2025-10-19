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

def solve():
    n = int(input())
    s = input().strip()
    
    res = 0
    for i in range(n):
        cnt = [0, 0, 0]
        for j in range(i, n):
            c = s[j]
            if c == '1':
                cnt[0] += 1
            elif c == '2':
                cnt[1] += 1
            elif c == '3':
                cnt[2] += 1
            
            if cnt[0] == cnt[1] == cnt[2]:
                    res += 1
                    
    return res

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep="\n")