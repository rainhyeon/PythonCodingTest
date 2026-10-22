def solution(numbers, target):
    count = 0
    
    def dfs(index, answer):
        nonlocal count
        
        if index == len(numbers):
            if answer == target:
                count += 1
            return
        
        dfs(index + 1, answer + numbers[index])
        dfs(index + 1, answer - numbers[index])
        
    dfs(0, 0)
    
    return count