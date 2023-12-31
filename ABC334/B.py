def main():
    A,M,L,R = map(int, input().split())

    res = 0

    if L <= A <= R:
        res += 1
        res += abs(L-A) // M
        res += abs(R-A) // M

    else:
        if A <= L:
            res += abs(R-A) // M - abs(L-A) // M
            if abs(L-A) % M==0:
                res += 1
        else:
            res += abs(L-A) // M - abs(R-A) // M
            if abs(R-A) % M==0:
                res += 1


        if L == 0 or R == 0:
            res += 1


    print(res)

if __name__ == '__main__':
    main()