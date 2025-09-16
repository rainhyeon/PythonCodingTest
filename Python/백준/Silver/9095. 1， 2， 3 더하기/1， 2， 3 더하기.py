# https://www.acmicpc.net/problem/9095
# 더하거나 안더하거나


N = int(input()) # 테스트 케이스 개수

count = 0
answer = []

def recur(num, sum):
    global count

    if num == sum:
        count += 1
        return 

    if num > sum:
        # 1 더하기 더하거나
        recur(num, sum + 1)
        # 2 더하기
        recur(num, sum + 2)
        # 3 더하기
        recur(num, sum + 3)

for i in range(N):
    count = 0
    num = int(input())
    recur(num, 0)
    answer.append(count)

for i in answer:
    print(i)