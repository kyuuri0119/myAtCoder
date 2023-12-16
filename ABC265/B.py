def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    # (X, Y)

    XY = {}
    for i in range(M):
        x, y = map(int, input().split())
        XY[x] = y

    for idx, a in enumerate(A):
        xy = XY.get(idx + 1)
        if xy:
            T += xy

        T -= a
        if T <= 0:
            print('No')
            break

        if idx + 2 == N:
            print('Yes')
            break


if __name__ == '__main__':
    main()
