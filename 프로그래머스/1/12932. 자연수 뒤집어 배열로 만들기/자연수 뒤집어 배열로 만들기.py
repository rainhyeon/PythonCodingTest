def solution(n):
    answer = []
    str_ans = str(n)
    for i in range(len(str_ans)):
        answer.append(int(str_ans[i]))
    answer.reverse()
    
    return answer