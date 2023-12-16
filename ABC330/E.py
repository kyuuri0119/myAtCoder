from collections import defaultdict


def main():
    N, Q = map(int,input().split())
    A = list(map(int,input().split()))

    d_count_A = defaultdict(int)
    not_A = set()
    for i in range(N+1):
        d_count_A[A[i]] += 1


    not_A = {i for i in range(0, N+1) if d_count_A[i]==0}

    for q in range(Q):
        i, x = map(int, input().split())
        i= i-1

        d_count_A[A[i]] -= 1

        if d_count_A[A[i]] == 0:
            not_A.add(A[i])

        if d_count_A[x] == 0:
            if x < N+1:
                not_A.remove(x)

        A[i] = x
        d_count_A[x] += 1

        print(min(not_A))


if __name__ == '__main__':
    main()