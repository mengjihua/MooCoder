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
    s = list(map(int, input().split()))
    if s == s[::-1]:
        return 0

    cnt1 = defaultdict(int)
    cnt2 = defaultdict(int)
    for i in range(n // 2):
        a, b = s[i], s[n - i - 1]
        if a == b:
            continue
        cnt1[a] += 1
        cnt1[b] += 1
        mx, mn = _max(a, b), _min(a, b)
        cnt2[(mx, mn)] += 1
    
    temp = 0
    cnt_keys = list(cnt1.keys())
    # for i in range(len(cnt_keys)):
    #     p1 = cnt_keys[i]
    #     for j in range(i, len(cnt_keys)):
    #         p2 = cnt_keys[j]
    #         if p1 == p2:
    #             t = cnt1[p1]
    #         else:
    #             key = (_max(p1, p2), _min(p1, p2))
    #             t = cnt1[p1] + cnt1[p2] - cnt2[key]
    #         temp = _max(temp, t)
    for p in cnt_keys:
        temp = _max(temp, cnt1[p])
    for p1, p2 in combinations(cnt_keys, 2):
        if p1 == p2:
            t = cnt1[p1]
        else:
            key = (_max(p1, p2), _min(p1, p2))
            t = cnt1[p1] + cnt1[p2] - cnt2[key]
        temp = _max(temp, t)
    return 2 * sum(cnt2.values()) - temp

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep="\n")