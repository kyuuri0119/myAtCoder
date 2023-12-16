import itertools

def main():
    n, m = map(int, input().split())

    l = [i for i in range(1, m+1)]

    c = itertools.combinations(l, n)
    for r in c:
        print(' '.join(map(str, list(r))))


if __name__ == '__main__':
    main()