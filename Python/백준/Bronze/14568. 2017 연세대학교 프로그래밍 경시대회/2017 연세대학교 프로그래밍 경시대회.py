n = int(input())
answer = 0

for a in range(n+1):
    for b in range(n+1):
        for c in range(n+1):
            if a + b + c == n:
                if c >= b+2:
                    if a != 0 and b != 0 and c != 0:
                        if a % 2 == 0:
                            answer += 1

print(answer)