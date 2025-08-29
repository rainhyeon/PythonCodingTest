n = int(input())

hint = [list(map(int, input().split())) for _ in range(n)]
# hint[0] = [123, 1, 1]
# [[123, 1, 1], [356, 1, 0] ....]

answer = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            
            if (a == b or b == c or c == a):
                continue
            
            cantidate = [a, b, c]

            cnt = 0
            for number, strike, ball in hint:
                # a, b, c를 비교했을때
                # 조건을 만족하면
                # strike 일때
                number = list(map(int, str(number)))

                ans_ball = 0
                ans_strike = 0

                for i in range(3):
                    if cantidate[i] == number[i]:
                        ans_strike += 1
                    else:
                        if cantidate[i] in number:
                            ans_ball += 1
               
                if ans_ball == ball and ans_strike == strike:
                    cnt += 1

            if cnt == n:
                answer += 1
print(answer)