import heapq

def solution(jobs):
    # 요청 시각 순으로 작업 정렬
    jobs.sort()
    
    current_time = 0   # 현재 시각
    total_turnaround_time = 0  # 총 반환 시간
    completed_jobs = 0  # 완료된 작업 수
    n = len(jobs)  # 작업 개수
    
    priority_queue = []  # 우선순위 큐 (소요 시간 기준 정렬)
    index = 0  # jobs 배열에서 처리할 작업의 인덱스
    
    while completed_jobs < n:
        # 현재 시간까지 요청된 작업을 우선순위 큐에 추가
        while index < n and jobs[index][0] <= current_time:
            request_time, duration = jobs[index]
            heapq.heappush(priority_queue, (duration, request_time))
            index += 1
        
        if priority_queue:
            # 우선순위 큐에서 소요 시간이 가장 적은 작업을 꺼냄
            duration, request_time = heapq.heappop(priority_queue)
            current_time += duration  # 작업 소요 시간만큼 현재 시간 증가
            total_turnaround_time += (current_time - request_time)  # 반환 시간 계산
            completed_jobs += 1
        else:
            # 우선순위 큐가 비어있으면 다음 작업 요청 시각으로 이동
            current_time = jobs[index][0]
    
    # 평균 반환 시간 계산 (정수 부분만 반환)
    return total_turnaround_time // n
