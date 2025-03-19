def solution(n):
    answer = 0
    list_ans = []
    str_ans = str(n)
    for i in str_ans:
        list_ans.append(i)
    list_ans.sort()
    list_ans.reverse()
    answer = int("".join(list_ans))
    return answer