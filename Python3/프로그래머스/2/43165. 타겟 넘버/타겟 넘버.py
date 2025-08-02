def solution(numbers, target):
    answer = 0
    def dfs(index, result):
        # 내부 함수에서 외부 변수(answer)를 수정할 수 있도록 선언
        nonlocal answer
        
        # 모든 수를 더하거나 뺐을때
        if index == len(numbers):
            # 결과 값과 같을 때
            if result == target:
                answer += 1
            # 조건이 맞든 아니든, 모든 숫자를 처리했으므로 탐색을 종료합니다.
            return
        
        # 아니면 무조건 더하거나 빼라
        dfs(index+1, result + numbers[index])
        dfs(index+1, result - numbers[index])
    
    dfs(0, 0)
    return answer
        