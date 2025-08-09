import sys

input = sys.stdin.readline

N, M = map(int, input().split())

uses = [int(input()) for _ in range(N)]

left = max(uses) # 하루치 최대 가격은 커버를 해야함
right = sum(uses)
answer = right

while left <= right:
    mid = (left + right) // 2
    count = 0
    money = 0

    # mid 값으로 uses를 더해가며 몇번 출금해야하는지
    for i in uses:
        if money < i: # 가지고 있는 돈 < 필요한 돈 보다 작으면
            count += 1 # 새로 출금
            money = mid
        money -= i # 돈 빠짐
    
    if count <= M: # 적게 꺼내도된다 -> K의 돈이 충분하다는 거니까 -> K 금액을 줄여보자
        answer = mid # 우리가 지향하는 것
        right = mid -1
    else: # 많이 꺼내야한다 -> K 금액이 너무 적으니까 -> K 금액을 늘려야한다
        left = mid + 1  
    
print(answer)


#┌─ count <= M ?
#│
#│   ├─ 예 (성공)
#│   │    → 지금 뽑는 금액 K로도 M번 이하로 N일 생활 가능
#│   │    → 한 번에 뽑는 돈을 조금 줄여도 여전히 M번 이하로 가능할 수 있음
#│   │    → 따라서 이 K를 "정답 후보"로 저장
#│   │    → 그리고 더 작은 K 쪽(왼쪽)으로 탐색
#│   │
#│   └─ 아니오 (실패)
#│        → 지금 뽑는 금액 K로는 M번보다 자주 인출해야 함
#│        → 즉 K가 너무 작아서 버티질 못함
#│        → 한 번에 뽑는 돈을 더 늘려야 함
#│        → 그래서 더 큰 K 쪽(오른쪽)으로 탐색

# nums.sort()하면 안됨
# 반례: 남은 돈을 다음날 이어 쓰는 흐름이 깨진다
# N=4, M=3
#uses = [9, 1, 9, 1]

#원래 순서 기준 최소 K = 10
#- K=9 → 인출 4번(실패)  / K=10 → 인출 2번(성공)

#정렬하면 [1,1,9,9]
#- K=9 → 인출 3번(성공)  ← 잘못해서 9가 답처럼 보임
