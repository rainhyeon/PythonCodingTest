def solution(n):
    answer = 0
    # n이 1일때를 고려해야한다!!
    
    
    for i in range(1, n+1):
        if pow(i, 2) == n:
            return pow(i+1,2)
        else:
            answer = -1
    return answer