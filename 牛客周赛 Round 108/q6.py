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

t = int(input())

# def solve():
#     n = int(input())
#     a = list(map(int, input().split()))
    
#     s = set()
    
#     for i in range(1, 1 << n):
#         sub = []
#         for j in range(n):
#             if (i >> j) & 1:
#                 sub.append(a[j])
#         sm = (1 << 15) - 1
#         for x in sub:
#             sm &= x
#         s.add(sm)
#     # print(s)

#     mx = max(s)
#     for i in range(1, mx + 1):
#         if i not in s:
#             return i
#     return mx + 1

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    def f(x):
        temp = []
        for num in a:
            if (num & x) == x:
                temp.append(num)
        if not temp:
            return False
        sm = (1 << 20) - 1
        for i in range(len(temp)):
            sm &= temp[i]
        return sm == x

    x = 1
    while f(x):
        x += 1
    return x


ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep="\n")