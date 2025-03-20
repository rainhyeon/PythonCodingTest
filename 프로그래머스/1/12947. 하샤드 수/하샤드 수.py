def solution(x):
    answer = True
    ans_map = map(int, str(x))
    
    if x % sum(ans_map) == 0:
        answer = True
    else:
        answer = False
    return answer