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

n1, n2 = map(int, input().split())

men = []
for i in range(n1):
    a, b, c, d, e = map(int, input().split())
    men.append((a, b, c, d, e))

women = []
for j in range(n2):
    f, g, h, k = map(int, input().split())
    women.append((f, g, h, k))

ans = []
for i in range(n1):
    a, b, c, d, e = men[i]
    for j in range(n2):
        f, g, h, k = women[j]
        if len({a, b, c, d, e, f, g, h, k}) == 9:
            ans.append(f"{i + 1} {j + 1}")
            
if not ans:
    print("None")
else:
    print(*ans, sep="\n")