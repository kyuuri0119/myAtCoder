def main():
    n = int(input())
    plist = list(map(int, input().split()))

    counter = 0
    i = n
    while i != 1:
        counter += 1
        i = plist[i - 2]
    print(counter)


if __name__ == '__main__':
    main()
