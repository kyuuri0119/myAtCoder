
def main():
    N, M = map(int, input().split())
    S = input()
    T = input()

    while True:
        f = S.find(T)
        if f>=0:
            # print(S[:f] + S[f + M:])
            S = S[:f]+S[f+M:]
        else:
            break

    if S == "":
        print('Yes')
    else:
        if S in T:
            print('Yes')
        else:
            print('No')

def main2():
    N, M = map(int, input().split())
    S = list(input())
    T = input()

    marked = "".join(['#' for s in T])

    used = [False]*N
    q = []

    def check(i):
        if used[i]:
            return

        if all([S[i+j] == T[j] or S[i+j] == "#" for j in range(0,M)]):
            used[i] = True
            q.append(i)

    for i in range(0,N-M+1):
        check(i)

    while q:
        i = q.pop()
        S[i:i+M] = marked

        for j in range(i-M, i+M+1):
            if 0<=j <N-M+1:
                check(j)


    if S == ["#"]*N:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main2()