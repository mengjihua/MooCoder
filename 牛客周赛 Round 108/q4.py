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

MOD = 998244353

t = int(input())

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    odd_cnt = sum(1 for x in a if x & 1)
    return (pow(2, n, MOD) - pow(2, odd_cnt, MOD)) % MOD

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep="\n")