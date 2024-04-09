import heapq
from collections import deque


def main():
    N, M, K = map(int, input().split())

    res = set()
    k = 1
    while len(res) <K:
        if N*k % M > 0:
            res.add(N*k)

        if M*k % N > 0:
            res.add(M*k)
        k+=1

    res = sorted(list(res))
    # print(res)
    print(res[K-1])





if __name__ == '__main__':
    main()