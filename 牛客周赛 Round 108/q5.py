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
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b

temp = [i * i for i in range(1, 100)]
tt = []
for t in temp:
    if reduce(lambda x, y: x + y, map(int, str(t))) in temp:
        tt.append(t)
# print(tt)

t = int(input())

# def solve():
#     n = int(input())
#     a = list(map(int, input().split()))
    
#     if n == 1:
#         return 1 if a[0] in tt else 0
    
#     sm = sum(a)
#     def dfs(i, cur_sm, cnt):
#         if i == n:
#             return cnt
#         res = -inf
#         for t in tt:
#             if cur_sm + t <= sm:
#                 res = _max(res, dfs(i + 1, cur_sm + t, cnt + 1))
#                 if res == n:
#                     break
#         return res
#     return dfs(0, 0, 0)

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 1:
        return 1 if a[0] in tt else 0
    
    sm = sum(a)
    
    dp = [inf] * (n + 1)
    dp[0] = 0
    
    for _ in range(n):
        for cnt in range(n):
            if dp[cnt] == inf:
                continue
            for t in tt:
                if dp[cnt] + t > sm:
                    continue
                if cnt + 1 <= n:
                    dp[cnt + 1] = _min(dp[cnt + 1], dp[cnt] + t)

    for x in range(n, -1, -1):
        if dp[x] <= sm - (n - x):
            return x
    return 0

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep="\n")