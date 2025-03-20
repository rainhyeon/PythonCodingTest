def solution(s):
    answer = ''
    list_ans = list(map(str, s))
    print(list_ans)
    if len(s) % 2 == 1:
        s_index = len(list_ans)//2
        answer = f"{list_ans[s_index]}"
    else:
        s_index = len(s)//2
        answer = f"{list_ans[s_index-1]}{list_ans[s_index]}"
    return answer