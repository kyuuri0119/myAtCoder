def main():
    A,B,D = map(int,input().split())

    res = [A]
    while True:
        if res[-1] + D > B:
            break
        res.append(res[-1]+D)

    print(*res)


if __name__ == '__main__':
    main()