def solution(distance, rocks, n):
    answer = 0
    
    # 거리의 최솟 값 -> mid
    rocks.append(distance)
    left = 1
    right = max(rocks)
    rocks.sort()
    
    while left <= right:
        mid = (left + right) // 2
        
        remove = 0
        prev = 0
        
        for rock in rocks:
            if rock - prev < mid:
                remove += 1
            else:
                prev = rock
                
        if remove > n: # 많이 제거됐다 -> mid를 최솟 값이 너무 작았다
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
                
    return answer