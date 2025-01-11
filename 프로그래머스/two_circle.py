import math

def solution(r1, r2):
    count = 0

    # x 좌표를 기준으로 가능한 y 좌표 계산
    for x in range(0, r2 + 1):
        # r2에서 가능한 y의 최대값
        y_max_r2 = math.floor(math.sqrt(r2**2 - x**2))
        # r1에서 가능한 y의 최소값 (작은 원의 내부 제외)
        y_min_r1 = math.ceil(math.sqrt(r1**2 - x**2)) if x < r1 else 0
    
        # 두 원 사이의 y 좌표 개수 계산
        count += (y_max_r2 - y_min_r1 + 1)
    count -= (r2-r1)+1
    # 대칭성을 고려하여 4배
    return count * 4
