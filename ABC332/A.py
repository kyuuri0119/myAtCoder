def main():
    N, S, K = map(int, input().split())

    res = 0
    for i in range(N):
        P, Q = map(int, input().split())
        res += P*Q

    if res >= S:
        print(res)
    else:
        print(res+K)

if __name__ == '__main__':
    main()