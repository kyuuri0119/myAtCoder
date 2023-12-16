import itertools


def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))

    comb = itertools.combinations(A, K)
    for c in comb:
        xor = None
        for idx, i in enumerate(c):
            if idx == 0:
                xor = i
            xor = int(bin(xor ^ i),2)

        print(bin(xor))



    # max_a = max(A)
    print()


if __name__ == '__main__':
    main()