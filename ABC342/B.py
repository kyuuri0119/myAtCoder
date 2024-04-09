def main():
    N = int(input())

    P = list(map(int, input().split()))
    pl = {p: i+1 for i, p in enumerate(P) }

    Q = int(input())

    for i in range(Q):
        a, b = map(int, input().split())
        if pl[a] > pl[b]:
            print(b)
        else:
            print(a)


if __name__ == '__main__':
    main()