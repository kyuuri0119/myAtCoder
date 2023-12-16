def main():

    N = list(map(int, input().split()))[0]
    D = list(map(int, input().split()))

    c = 0

    for n in range(1,N+1):
        if len(str(n)) > 1:
            if not all([s==str(n)[0] for s in str(n)]):
                continue

        for d in range(1,D[n-1]+1):
            if len(str(d)) > 1:
                if not all([s==str(d)[0] for s in str(d)]):
                    continue

            if str(n)[0] == str(d)[0]:
                c += 1

    print(c)


if __name__ == '__main__':
    main()

