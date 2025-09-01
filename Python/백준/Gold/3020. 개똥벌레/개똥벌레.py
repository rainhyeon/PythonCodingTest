import sys
input = sys.stdin.readline

N, H = map(int, input().split()) # N: 새로, H: 가로

arr = []
answer = []
sum = 0

line = [0 for _ in range(H)]

for t in range(N):
    height = int(input())
    if t % 2 == 0:
        line[0] += 1
        line[height] -= 1

    else:
        line[H-height] += 1
    
prefix = [0 for _ in range(H+1)]

for i in range(H):
    prefix[i+1] = prefix[i] + line[i]

prefix = prefix[1:]

print(f"{min(prefix)} {prefix.count(min(prefix))}")