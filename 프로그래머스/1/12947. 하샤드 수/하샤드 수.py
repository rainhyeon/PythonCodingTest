def solution(x):
    answer = True
    list_ans = []
    sum_ans = 0
    
    str_ans = str(x)
    print(str_ans)
    for i in str_ans:
        list_ans.append(int(i))
    
    for i in list_ans:
        sum_ans += i
    
    if x % sum_ans == 0:
        answer = True
    else:
        answer = False
    return answer