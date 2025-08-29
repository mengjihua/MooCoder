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
    n, m, k = map(int, input().split())
    equips = []
    equip_set = set()
    for _ in range(k):
        r, c = map(int, input().split())
        equips.append((r, c))
        equip_set.add((r, c))
    
    cx, cy = (n + 1) // 2, (m + 1) // 2
    candidates = []
    for dx in range(-2, 3):
        for dy in range(-2, 3):
            x, y = cx + dx, cy + dy
            if 1 <= x <= n and 1 <= y <= m and (x, y) not in equip_set:
                candidates.append((x, y))
    
    if not candidates:
        for x in range(1, n + 1):
            for y in range(1, m + 1):
                if (x, y) not in equip_set:
                    candidates.append((x, y))
    
    pairs = []
    for i in range(k):
        for j in range(i + 1, k):
            r1, c1 = equips[i]
            r2, c2 = equips[j]
            dist = abs(r1 - r2) + abs(c1 - c2)
            pairs.append((r1, c1, r2, c2, dist))
    
    ans = None
    min_coverage = inf
    
    for (x, y) in candidates:
        coverage = 0
        for (r1, c1, r2, c2, dist) in pairs:
            d1 = abs(x - r1) + abs(y - c1)
            d2 = abs(x - r2) + abs(y - c2)
            if d1 + d2 == dist:
                coverage += 1
        if coverage < min_coverage:
            min_coverage = coverage
            ans = (x, y)
    
    return ans

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep="\n")