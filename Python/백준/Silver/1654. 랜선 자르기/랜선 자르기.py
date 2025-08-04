import sys

input = sys.stdin.readline

K, N = map(int, input().split())
lines = []
answer = 0
count = 0

for i in range(K):
    lines.append(int(input()))

left = 1 # 최소 길이
right = max(lines) # 최대 길이

while left <= right:
    mid = (left + right) // 2 # 중간 길이 값
    count = sum(i//mid for i in lines) # 총 잘리는갯수
    #print(f"left: {left}, right: {right}, mid: {mid}, N: {N}, count: {count}, answer: {answer}")
    if count >= N:
        answer = mid
        left = mid + 1
    else:
        right = mid -1

print(answer)