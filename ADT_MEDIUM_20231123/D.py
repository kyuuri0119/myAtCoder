import sys

sys.setrecursionlimit(1_000_000)

def main():
    N, X = map(int, input().split())
    A = list(map(int,input().split()))

    used = [0]* N
    r = 0

    def dfs(i, c):
        if used[i-1]:
            return c
        else:
            c+=1
            used[i-1] = 1
            return dfs(A[i-1],c)

    r = dfs(X,0)

    print(r)

if __name__ == '__main__':
    main()
