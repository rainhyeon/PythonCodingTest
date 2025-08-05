def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance) # 마지막 최종 거리 추가
    rocks.sort()
    
    left = 1
    right = distance

    
    while left <= right:
        mid = (left + right) // 2 # 최솟값 후보
        prev = 0  # 이전 rock
        remove = 0 # 제거된 rock 개수
        
        for rock in rocks:
            if rock - prev < mid: # 현재꺼 - 이전꺼 < 최소값 후보: 최솟값보다 더 적어지면 안되니까
                remove += 1 # 제거한다
            else:               
                prev = rock # 다음 rock에 대해 계산 
        
        if remove <= n:     # 최솟값이 너무 커서 많이 제거하지 않았네
            left = mid + 1  # 최솟값을 줄이자
            answer = mid    # 바위 제거 수가 n 이하일때 성공
        else:               # 최솟값이 너무 작아서 많이 제거했다
            right = mid -1  # 최솟값을 높이자
    
    return answer