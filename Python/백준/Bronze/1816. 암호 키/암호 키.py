n = int(input())
nums = [int(input()) for _ in range(n)]


def is_prime(num):
    for i in range(2, 1_000_001):
        if num % i == 0:
            print("NO")
            break
        if i == 1_000_000:
            print("YES")


for num in nums:
    is_prime(num)



