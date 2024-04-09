import sys

sys.setrecursionlimit(1_000_000_000)


def main():
    T = input()
    N = int(input())

    bag ={}
    for i in range(N):
        bag[i] = set(map(str, input().split()))

    res =set()

    def dfs(cost, i, t:str):
        # print(cost, i, t)
        if i == N:
            if t=='':
                res.add(cost)

            return

        if (N-i)*10<len(t):
            return

        for j in range(1, min(11, len(t)+1)):
            if t[0:j] in bag[i]:
                dfs(cost+1, i+1, t[j:])

        # for s in bag[i]:
        #     if t.startswith(s):
        #         dfs(cost+1, i+1, t[len(s):])

        dfs(cost, i+1, t)

    dfs(0, 0, T)

    if len(res) == 0 or (m := min(res)) == 0:
        print(-1)
    else:
        print(m)


if __name__ == '__main__':
    main()