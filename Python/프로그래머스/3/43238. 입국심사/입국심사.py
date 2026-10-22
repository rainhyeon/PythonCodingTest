def solution(n, times):
    answer = 0
    
    left = 1
    right = max(times) * n
    
    while left <= right:
        mid = (left + right) // 2 # 심시 받는데 걸리는 시간
        
        count = sum((mid // i) for i in times)
        
        if count >= n: # 사람이 많다 -> 줄여야한다
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
        
    return answer