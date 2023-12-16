import heapq
import sys

sys.setrecursionlimit(1_000_000)


def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    first = [0] * N

    for idx, t in enumerate(T):
        mf = min(first)
        if  mf>0 and mf <= t:
            continue

        def dfs(t, i, start):
            if i != start and start % (N - 1) == i:
                return

            if i > N - 1:
                i = i % (N - 1)

            if 0 < first[i] <= t:
                return

            first[i] = t
            return dfs(t + S[i], i + 1, start)

        dfs(t, idx, idx)

    for f in first:
        print(f)

def after():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    ans = [0]*N

    heapq_list = [(t, i) for i,t in enumerate(T)]
    heapq.heapify(heapq_list)

    # print(heapq_list)

    while heapq_list:
        poped = heapq.heappop(heapq_list)
        i = poped[1] % N
        t = poped[0]
        # print(i, t, ans[i])
        if ans[i]>0 and ans[i] < t:
            continue
        ans[i] = t
        heapq.heappush(heapq_list, (t+S[i], i+1))
        # print(heapq_list)

    for a in ans:
        print(a)




if __name__ == '__main__':
    # main()

    after()