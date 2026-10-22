def solution(triangle):
    rev = triangle[::-1]

    for y in range(len(rev)-1):
        for x in range(len(rev[y])-1):
            rev[y+1][x] += max(rev[y][x], rev[y][x+1]) # 위에꺼는 아래꺼들의 합 
        
    print(rev[-1][0]) 
    return rev[-1][0]#맨아래 꼭지점