from typing import List

mod = 998244353


def main():
    N = int(input())
    A = list(map(int, input().split()))

    i = 1
    count = 0

    expected = [0]*N
    accumlation_expected = [0]*(N+1)
    for i in range(N-2, -1, -1):
        e = 0
        for j in range(1, A[i]):
            e+= expected[i+j] + 1
        expected[i] = pow(e /(A[i] + 1))
        print(expected[i])

    print(expected[0]%mod)


if __name__ == '__main__':
    main()
