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
    s = input()
    # "qcjj"子序列的数列和"qcay"子序列的数量
    q_cnt = qc_cnt = qcj_cnt = qcjj_cnt = 0
    qca_cnt = qcay_cnt = 0
    for c in s:
        if c == 'q':
            q_cnt += 1
        elif c == 'c':
            qc_cnt += q_cnt
        elif c == 'a':
            qca_cnt += qc_cnt
        elif c == 'y':
            qcay_cnt += qca_cnt
        elif c == 'j':
            qcjj_cnt += qcj_cnt
            qcj_cnt += qc_cnt
    
    if qcjj_cnt > qcay_cnt:
        return 'qcjj'
    else:
        return 'qcay'

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep="\n")