def main():
    N = int(input())
    A = list(map(int, input().split()))

    minA = A.index(min(A))
    l = {p: i+1  for i, p in enumerate(A)}

    res = [0]*N

    pos = minA
    res[0] = pos+1

    for i in range(1, N):

        res[i] = l[res[i-1]]

    print(*res)




if __name__ == '__main__':
    main()