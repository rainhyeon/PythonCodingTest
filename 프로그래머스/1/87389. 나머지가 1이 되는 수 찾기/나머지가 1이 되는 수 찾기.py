def solution(n):
    answer = 0
    num = 0
    for i in range(1, n):
        if n % i == 1:
            num = i
            break
    answer = num
    return answer