# 조건을 만족하면서, 비용을 최소


N = int(input()) # 개수

_dan, _ji, _tan, _vi = map(int, input().split())

ingre = [list(map(int, input().split())) for _ in range(N)]
#print(ingre)
answer = 9999999
used_ingre = []
used_answer = []

def recur(idx, dan, ji, tan, vi, price):
    global answer
    global used_answer
    global used_ingre

    if dan >= _dan and ji >= _ji and tan >= _tan and vi >= _vi:
        if answer > price: # 더 저렴하면 업데이트
            answer = min(answer, price)
            used_answer = []
            for i in used_ingre: # 마구잡이로 넣은게 최소값이라면 그 안에있는걸 정답 리스트에 넣어준다
                used_answer.append(i+1)
            #print(f"price 업데이트: {price}, {used_answer}/ {used_ingre}")
        return
    
    if idx == N:
        return

    # 넣는 경우
    used_ingre.append(idx)
    #print(f"{idx} 넣기 {used_ingre}")
    recur(idx+1, dan+ingre[idx][0], ji+ingre[idx][1], tan+ingre[idx][2], vi+ingre[idx][3], price+ingre[idx][4])

    # 안넣는 경우
    used_ingre.pop()
    #print(f"{idx} 빼기 {used_ingre}")
    recur(idx+1, dan, ji, tan, vi, price)

recur(0,0,0,0,0,0)

used_answer.sort() # 정렬까지

if used_answer:
    print(answer)
    print(*used_answer)
else:
    print(-1)