# 완전 탐색(브루트포스)
# 9C7가지로 출력
from itertools import combinations
import sys

input = sys.stdin.readline

hats = [int(input()) for _ in range(9)]

for comb in combinations(hats, 7):
    if sum(comb) == 100:
        for n in sorted(comb):
            print(n)
        break