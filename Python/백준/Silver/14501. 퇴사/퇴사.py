# 최대 이익을 출력해랴

N = int(input()) # 개수
works = [list(map(int, input().split())) for _ in range(N)]
#print(works)
answer = -999999999

def recur(index,price):
    global answer
    #print(f"{index}, {price}")

    if index > N-1: # 범위를 넘어가면(N부터)
        if index > N: return # 퇴사한 날 이후라면 최댓값 새로 갱신하지말고, 이전의 최댓값을 출력해라
        # print(price)
        answer = max(answer, price) # 퇴사날 마지막날이후(N)이면 최댓값 계산을 해라
        return

    # 상담 한다면
    recur(index+works[index][0], price+works[index][1])

    # 상담 안한다면
    recur(index+1, price)

recur(0, 0)
print(answer)


