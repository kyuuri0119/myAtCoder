
def main():
    N, K= map(int, input().split())
    A = list(map(int, input().split()))

    res = []

    for a in A:
        if a % K == 0:
            res.append(a//K)

    print(*res)


if __name__ == '__main__':
    main()