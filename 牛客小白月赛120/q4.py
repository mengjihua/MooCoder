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
#     n, m = map(int, input().split())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
    
#     if n > m:
#         return -1
    
#     if a == b:
#         return 0
    
#     group_a = []
#     group_b = []
#     i, j = 0, 0
#     while True:
#         if a[i] != b[j]:
#             return -1
        
#         cnt_a, cnt_b = 0, 0
#         while i < n - 1 and a[i] == a[i + 1]:
#             cnt_a += 1
#             i += 1
#         while j < m - 1 and b[j] == b[j + 1]:
#             cnt_b += 1
#             j += 1
            
#         if cnt_a == 0 and cnt_b == 0:
#             break
#         elif cnt_a == 0:
#             return -1
#         elif cnt_b == 0:
#             return -1
        
#         if cnt_a > cnt_b:
#             return -1
        
#         group_a.append(cnt_a)
#         group_b.append(cnt_b)
        
#     if a[n - 1] != b[m - 1]:
#         return -1
        
#     if a[n - 1] == a[n - 2]:
#         group_a[-1] += 1
#         group_b[-1] += 1
    
#     max_k = -1
#     for i, j in zip(group_a, group_b):
#         k = (j * (i - 1) + i - 1) // i
#         max_k = _max(max_k, k)

#     return max_k

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    
    cnt_a = defaultdict(int)
    cnt_b = defaultdict(int)
    for num in a:
        cnt_a[num] += 1
    for num in b:
        cnt_b[num] += 1
        
    for num in set(b):
        if cnt_a[num] == 0:
            return -1
        
    i = 0
    j = 0
    temp = [False] * m
    while i < n and j < m:
        if a[i] == b[j]:
            temp[j] = True
            i += 1
            j += 1
        else:
            j += 1
            
    if i < n:
        return -1
        
    for j in range(1, m):
        if not temp[j]:
            if b[j] != b[j - 1]:
                return -1

    res = 0
    for num in set(b):
        if cnt_b[num] <= cnt_a[num]:
            continue
        k = (cnt_b[num] + cnt_a[num] - 1) // cnt_a[num]
        r = 0
        power = 1
        while power < k:
            r += 1
            power *= 2
        if r > res:
            res = r
            
    return res

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep="\n")