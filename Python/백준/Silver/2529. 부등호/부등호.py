k = int(input())
sign = input().split(" ")
result = []
used = [False] * 10

def check(a, b, op):
    if op == '>' :
       return a > b
    else:
        return a < b

# idx: 현재 숫자 (0~9)
# num: 현재까지 만든 문자열
def backtraking(idx, num):
    if idx == k+1:
        result.append(num)
        return
    
    #0~9까지 탐색
    for i in range(10):
        if used[i]:
            continue
        if idx == 0 or check(int(num[-1]), i, sign[idx-1]):
            used[i] = True
            backtraking(idx+1, num+str(i))
            used[i] = False
        
backtraking(0, "")
print(result[-1])
print(result[0])