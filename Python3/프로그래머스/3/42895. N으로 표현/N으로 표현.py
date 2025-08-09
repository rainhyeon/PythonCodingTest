def solution(N, number):
    answer = 0
    if N == number:
        return 1
    
    # 중복 값 없애기 위해서 set 사용
    S = [set() for _ in range(9)] # 1~8까지
    
    # N 사용 횟수
    for i in range(1, 9):
        concat = int(str(N)*i)
        S[i].add(concat)
        
        # 만약 이어붙인게 같다면
        if concat == number:
            return i
        
        for j in range(1, i):
            for a in S[j]:
                for b in S[i-j]:
                    S[i].add(a+b)
                    S[i].add(a-b)
                    S[i].add(b-a)
                    S[i].add(a*b)
                    if b != 0:
                        S[i].add(a//b)
                    if a != 0:
                        S[i].add(b//a)
                        
        if number in S[i]:
            return i
    
    return -1