# 최대 이익을 출력해랴

N = int(input()) # 개수
works = [list(map(int, input().split())) for _ in range(N)]
#print(works)
answer = -999999999

def recur(index,price):
    global answer
    #print(f"{index}, {price}")

    if index == N: # 범위를 넘어가면(N부터)
        answer = max(answer, price) # 퇴사날 마지막날이후(N)이면 최댓값 계산을 해라
        return
    if index > N:
        return

    # 상담 한다면
    recur(index+works[index][0], price+works[index][1])

    # 상담 안한다면
    recur(index+1, price)

recur(0, 0)
print(answer)


