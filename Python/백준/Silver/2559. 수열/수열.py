def solution(tem_list, len, k):
    sum_tem = 0
    max_sum = 0
    stack_list = []
    sum_tem = sum(tem_list[:k])
    max_sum = sum_tem

    for i in range(k, len):
        sum_tem = sum_tem - tem_list[i-k] + tem_list[i]
        max_sum = max(max_sum, sum_tem)
    
    return max_sum

def main():
    n, m = map(int, input().split())
    # 리스트 받기
    tem_list = list(map(int, input().split()))
    print(solution(tem_list, n, m))

if __name__ == "__main__":
    main()