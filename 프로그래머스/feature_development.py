from math import ceil
def solution(progresses, speeds):
    answer = []
    left_chore = []
    num = 1
    
    left_chore = [ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    for i in range(len(left_chore)):
        try:
            if left_chore[i] < left_chore[i+1]:
                answer.append(num)
                num = 1
            else:
                left_chore[i+1] = left_chore[i]
                num += 1
        except:
            answer.append(num)
            
    return answer
