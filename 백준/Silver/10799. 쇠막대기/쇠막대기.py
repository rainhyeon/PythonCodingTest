def main():
    input_str = input()
    result = []
    count = 0

    result.append(input_str[0])
    for i in range(1, len(input_str)):
        if input_str[i] == '(':
            result.append(input_str[i])
        else :
            if input_str[i-1] == '(':
                result.pop()
                count += len(result)
                #print(count)
            else:
                result.pop()
                count += 1

    print(count)

if __name__ == "__main__":
    main()