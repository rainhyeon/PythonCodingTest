def solution(n, times):
    answer = 0
    count = 0
    
    left = 1 # 최소 시간
    right = max(times) * n # 최대 시간
    print(right)
    
    while left <= right:
        mid = (left + right) // 2
        count = 0
        for i in times:
            count += (mid // i)
        print(f"mid: {mid}, n: {n}, count: {count}, left: {left}, right: {right}")
        if count < n:
            left = mid + 1
            print("작다")
        else:
            answer = mid
            right = mid -1
            
    return answer
        
# 문제 : count == n인 경우가 없을 수 도 있다
# count >= n 일때 n과 가장 가까운 count를 찾아야한다
# 그러므로 count >= n 일때 answer에 mid 값을 저장해두어야한다.