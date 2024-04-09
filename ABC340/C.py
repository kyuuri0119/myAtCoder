import math
import sys
from functools import cache

sys.setrecursionlimit(20000000)

def main():
    N = int(input())

    memo = {}

    def dfs(cost, now):

        if c := memo.get(now):
            return c

        add = now / 2
        _cost = cost
        if (a := math.floor(add)) >= 2:
            _cost += dfs(cost, a)

        if (b := math.ceil(add)) >= 2:
            _cost += dfs(cost, b)

        _cost += now
        memo[now] = _cost
        return _cost

    print(dfs(0, N))

def after():
    N = int(input())

    @cache
    def f(N):
        return 0 if N==1 else N+ f(floor(N,2)) + f(ceil(N,2))

    @cache
    def floor(N, div):
        return N//div

    @cache
    def ceil(N, div):
        return (N+div-1)//div

    print(f(N))


if __name__ == '__main__':
    # main()
    after()
