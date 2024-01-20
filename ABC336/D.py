def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.insert(0, 0)
    A.append(0)

    l, r = [0]*(N+2), [0]*(N+2)
    for i in range(1, N+1):
        l[i] = min(l[i-1]+1,A[i])
        r[-(i+1)] = min(r[-i]+1, A[-(i+1)])

    # print(A)
    # print(l)
    # print(r)

    ans = 0
    for i in range(1, N+1):
        now = min(l[i], r[i])
        ans = max(ans, now)

    print(ans)


if __name__ == '__main__':
    main()