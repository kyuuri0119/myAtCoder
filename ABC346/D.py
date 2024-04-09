import itertools
import sys

sys.setrecursionlimit(1_000_000_000)


def main():
    N= int(input())
    S= input()
    C = list(map(int, input().split()))

    pat = "01"*(N//2) + "0"*(N%2)
    print(S.encode() ^ pat.encode())








if __name__ == '__main__':
    main()