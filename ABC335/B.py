import itertools


def main():
    N = int(input())

    l = [i for i in range(N+1)]

    for a in l:
        for b in l:
            for c in l:
                if a+b+c<=N:
                    print(a, b, c)


if __name__ == '__main__':
    main()