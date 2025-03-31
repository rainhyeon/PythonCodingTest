import sys
def is_prime(x, y):
    is_prime = [True] * (y+1) #0인덱스 때문에
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(y **0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, y+1, i):
                is_prime[j] = False

    for num in range(x, y+1):
        if is_prime[num]:
            print(num)


def main():
    # 입력 받기
    m, n = map(int, sys.stdin.readline().split())

    # 소수 구하기
    is_prime(m, n)

if __name__ == "__main__":
    main()