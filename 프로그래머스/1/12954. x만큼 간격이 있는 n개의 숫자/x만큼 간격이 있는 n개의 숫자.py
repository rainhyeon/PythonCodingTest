def solution(x, n):
    answer = []
    # range의 3번째 인자가 0이면 안된다
    if x < 0:
        for i in range(x, n*x-1, x):
            answer.append(i)
    elif x > 0: 
        for i in range(x, n*x+1, x):
            answer.append(i)
    else:
        for i in range(n):
            answer.append(0)   
    print(answer)
    return answer