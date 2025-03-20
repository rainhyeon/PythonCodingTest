def solution(arr):
    answer = []
    
    arr_2 = [i for i in arr]
    arr_2.sort()
    
    if len(arr) == 1:
        answer.append(-1)
    else:
        arr.remove(arr_2[0])
        answer = [i for i in arr]
    
    return answer