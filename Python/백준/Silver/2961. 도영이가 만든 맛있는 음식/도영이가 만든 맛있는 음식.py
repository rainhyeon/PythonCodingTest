N = int(input()) # 개수

taste = [list(map(int, input().split())) for _ in range(N)]

answer = 99999999

# use: 한번이라도 섞어야하니까 , 섞는 개수 체크
def recur(index, shin, zzan, use):
    global answer

    if index == N:
        if use > 0:
            answer = min(answer, abs(shin-zzan))
        return    

    # 넣는다
    recur(index+1, shin * taste[index][0], zzan + taste[index][1], use+1)

    # 안넣는다
    recur(index+1, shin, zzan, use)


recur(0,1,0,0)
print(answer)