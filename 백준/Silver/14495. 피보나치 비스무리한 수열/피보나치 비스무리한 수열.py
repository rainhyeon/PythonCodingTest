def fibor(num, result):
    add_num = result[num-1]+result[num-3]
    result.append(add_num)

def main():
    # 입력 받기
    n = int(input())
    result = [1] * 3

    # 피보나치 구하기기
    for i in range(3, n):
        fibor(i, result)
    
    print(result.pop())

if __name__ == "__main__":
    main()