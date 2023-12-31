import itertools


def main():
    N,K = map(int, input().split())

    A = list(map(int, input().split()))

    is_odd = bool(len(A)%2)

    res = []
    if is_odd:
        for a in A:
            pass
    else:
        res = 0
        for i in range(0, len(A), 2):
            res += A[i+1] - A[i]

        print(res)

if __name__ == '__main__':
    main()