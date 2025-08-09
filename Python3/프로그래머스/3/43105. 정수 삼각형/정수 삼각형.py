def solution(triangle):
    answer = 0
    
    lines = triangle[-1][:]
    
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            lines[j] = triangle[i][j] + max(lines[j], lines[j+1])
            
        
    return lines[0]