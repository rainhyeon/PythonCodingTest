def solution(phone_number):
    answer = ''
    
    last_len = len(phone_number) - 4
    
    answer += '*'*last_len + phone_number[-4:]
    print(answer)
    return answer