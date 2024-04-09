def main():
    N = int(input())

    G = []
    for i in range(N):

        l = list(map(int, input().split()))
        G.append(l)

    for i in range(N):
        res = []
        for j in  range(N):
            if G[i][j]:
                res.append(j+1)
        if res:
            print(*sorted(res))



if __name__ == '__main__':
    main()