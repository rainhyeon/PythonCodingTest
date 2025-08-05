import sys

input = sys.stdin.readline

N, C = map(int, input().split())
X = []

for i in range(N):
    X.append(int(input()))

X.sort()

left = 1
right = X[-1] - X[0]
answer = 0

while left <= right:
    mid = (left + right) // 2 # 거리의 최댓값

    pre = min(X)
    count = 1 # 첫 집에는 항상 공유기 하나 설치하고 시작해야 함

    for i in X:
        if i - pre >= mid: # 거리가 충분하면 설치(최대값이면)
            count += 1
            pre = i # 최신 공유기 위치 갱신

    if count >= C:  # 개수가 더 많으면 -> 최댓값이 작다는말
        left = mid + 1 # 늘린다
        answer = mid # 최댓값이 되도록 하는 방향이니까 성공?
    else:
        right = mid -1
    
print(answer)