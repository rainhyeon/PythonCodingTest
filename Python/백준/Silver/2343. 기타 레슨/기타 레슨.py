import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lectures = list(map(int, input().split()))

left = max(lectures)
right = sum(lectures)
answer = right

while left <= right:
    mid = (left + right) // 2
    total = 0 # 초기화 while 문 안에서
    count = 1 # 초기화 while 문 안에서

    for l in lectures:
        if total + l > mid:
            count += 1
            total = l
        else:
            total += l
    
    if count <= M:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
