def main():
    n = int(input())
    pattern = input()
    parts = pattern.split('*')
    prefix = parts[0]
    suffix = parts[1]

    for _ in range(n):
        word = input()
        if len(word) < len(prefix) + len(suffix):
            print("NE")
            continue

        if word.startswith(prefix) and word.endswith(suffix):
            print("DA")
        else:
            print("NE")


if __name__ == "__main__":
    main()
