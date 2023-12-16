from functools import reduce
from operator import xor


def main():
    N=int(input())
    A = list((map(int,input().split())))
    max_a = max(A)

    kl = []

    for k in reversed(range(2, max_a)):
        A_ = list(A)
        for i, a in enumerate(A):
            if a>k:
                cc = a//k
                for c in range(cc):
                    A_.append(k)
                A_[i]=a-cc*k
                A_[i]=a-k
        print(A_)
        S = reduce(xor, A_)
        print(k, S)
        if S!=0:
            kl.append(k)


    if len(kl) == max_a-1:
        print(-1)
    elif len(kl):
        if reduce(xor, A) != 0:
            print(-1)
        else:
            print(kl[0])
    else:
        print(0)


if __name__ == '__main__':
    main()