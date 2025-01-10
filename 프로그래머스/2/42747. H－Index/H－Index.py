def solution(citations):
    citations.sort(reverse=True)  # 내림차순 정렬
    print(citations)

    for i in range(len(citations)):
        # i번째 논문의 인용 횟수가 (i + 1)번 이상인지 확인
        if citations[i] < i + 1:
            return i

    # 모든 논문이 조건을 만족하는 경우
    return len(citations)
