from pprint import pprint


def main():
    N, Q = map(int, input().split())

    # P = [list(input()) for n in range(N)]

    P = []
    for n in range(N):
        line = list(input())

        P.append([1 if w=='B' else 0 for w in line])

    # print(P)

    for q in range(Q):
        A, B, C, D = map(int, input().split())

        res = 0
        memo = {}
        t = 0
        d = N

        if C//N - A//N == 0:
            t = min(A%N, C%N)
            d = max(A%N, C%N)

        # print(t, d)
        for r in range(t, d):

            if (D // N - B // N) == 0:
                row_bd = P[r % N][B % N :D % N+1]
                memo[r % N] = sum(row_bd)
            else:
                row_l = P[r % N][B % N :]
                # print(row_l)
                row_r = P[r % N][0: D % N+1]
                # print(row_r)
                memo[r% N] = sum(row_l) + sum(row_r)
                if (D//N - B//N) > 1:
                    # 1区画フルで挟む場合
                    memo[r% N] += sum(P[r%N])*(D//N - B//N -1)

            # res += memo[r% N]

        if C // N - A // N == 0:
            for r in range(A//N, C//N+1):
                res += memo.get(r % N)
        else:
            for r in range(A%N, N):
                res += memo.get(r % N)
            for r in range(0, C%N+1):
                res += memo.get(r % N)

            if (C // N - A // N) > 1:
                res += sum(memo.values()) * (C // N - A // N - 1)

        print(res)

def after():
    N, Q = map(int, input().split())

    # P = [list(input()) for n in range(N)]

    P = []
    for n in range(N):
        line = list(input())

        P.append([1 if w=='B' else 0 for w in line])

    cum_sum = [[0]*(N+1) for i in range(N+1)]
    for i in range(N):
        for j in range(N):
            cum_sum[i+1][j+1] = cum_sum[i][j+1] + cum_sum[i+1][j] + P[i][j] - cum_sum[i][j]

    def g(h,w):
        # if h<=N and w <=N:
        #     return cum_sum[h][w]
        #
        ret = 0
        ret1 = cum_sum[N][N] * (h//N) * (w//N)
        ret2 = cum_sum[h%N][N] * (w // N)
        ret3 = cum_sum[N][w%N] * (h // N)
        ret4 = cum_sum[h%N][w%N]
        return ret1 + ret2 + ret3 + ret4

    def solve(A, B, C, D):
        # return g(C,D) + g(A, B) - g(C, B) - g(A, D)
        a1 = g(C,D)
        a2 = g(A,B)
        a3 = g(C, B)
        a4 = g(A,D)
        return a1 + a2 - a3 - a4

    for q in range(Q):
        A, B, C, D = map(int, input().split())
        print(solve(A,B, C+1, D+1))


if __name__ == '__main__':
    # main()
    after()