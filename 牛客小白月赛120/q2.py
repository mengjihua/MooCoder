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


class PrimeSieve:
    def __init__(self, max_n=0):
        """初始化时可预计算max_n范围内的素数表"""
        self.max_n = max_n
        self.is_prime, self.primes = self.sieve_eratosthenes(max_n) 

    def sieve_eratosthenes(self, n: int) -> List[int]:
        """埃氏筛法，时间复杂度 O(n log log n)"""
        if n < 2:
            return [False] * (n + 1), []
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return is_prime, [i for i in range(n + 1) if is_prime[i]]

    def sieve_euler(self, n: int) -> List[int]:
        """欧拉筛法（线性筛），时间复杂度 O(n)"""
        if n < 2:
            return []
        is_prime = [True] * (n + 1)
        primes = []
        is_prime[0] = is_prime[1] = False

        for i in range(2, n + 1):
            if is_prime[i]:
                primes.append(i)
            for p in primes:
                if i * p > n:
                    break
                is_prime[i * p] = False
                if i % p == 0:
                    break
        return primes
    
    def judge_prime(self, n: int) -> bool:
        """判断一个数是否为素数, 时间复杂度 O(√n)"""
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return n >= 2
    
is_prime = PrimeSieve(2 * 10 ** 4 + 1).is_prime

t = int(input())

def solve():
    x = int(input())
    
    if x == 1:
        return -1
    
    for y in range(1, x):
        xor = x ^ y
        if not is_prime[xor] and xor > 2:
            return y

    return -1

ans = []
for _ in range(t):
    ans.append(solve())
print(*ans, sep="\n")