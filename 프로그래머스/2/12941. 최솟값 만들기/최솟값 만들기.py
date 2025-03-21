def solution(A,B):
    answer = 0
    min_ans = 0
    A.sort()
    B.sort()
    B.reverse()
    
    print(f"A: {A}, B: {B}")
    
    for i in range(len(A)):
        answer += A[i] * B[i]
        
    return answer
