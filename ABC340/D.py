from collections import deque


def main():
    N = int(input())
    A = [0]*(N+1)
    B = [0]*(N+1)
    X = [0]*(N+1)
    res = [0]*(N+2)
    # res[0]=0

    for i in range(N-1):
        a, b, x = map(int, input().split())
        A[i+1], B[i+1], X[i+1] = a, b, x

    Q = deque()
    Q.append(1)




    while len(Q):
        s = Q.popleft()
        if s >= N:
            continue
        next_a = s+1
        next_b = X[s]
        # print(s, next_a, next_b, res)
        if res[next_a]==0:
            res[next_a] = res[s]+A[s]
            Q.append(next_a)

        else:
            if res[next_a] > res[s]+A[s]:
                res[next_a] = res[s]+A[s]
                Q.append(next_a)

        if res[next_b] == 0:
            res[next_b] = res[s]+B[s]
            Q.append(next_b)
        else:
            if res[next_b] > res[s]+B[s]:
                res[next_b] = res[s]+B[s]
                Q.append(next_b)

    print(res[N])



if __name__ == '__main__':
    main()