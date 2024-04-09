import itertools
import sys
from collections import deque

sys.setrecursionlimit(1_000_000_000)


def main():
    H, W = map(int, input().split())
    G = []
    s = ()
    t = ()
    for h in range(H):
        A = input()
        G.append(list(A))

        if not s and (sw := A.find('S')) != -1:
            s = (h, sw)

        if not t and (tw := A.find('T')) != -1:
            t = (h, tw)

    N = int(input())

    drag = [[0] * W for i in range(H)]
    for i in range(N):
        r, c, e = map(int, input().split())
        drag[r - 1][c - 1] = e

    energy = 0
    used = []
    if e := drag[s[0]][s[1]]:
        energy = e
        used = [(s[0], s[1])]
        G[s[0]][s[1]] = '#'

    queue = deque([[s, energy, G.copy()]])
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while queue:
        now = queue.pop()
        # print(now)

        if now[0] == t:
            print('Yes')
            return

        if (e := drag[now[0][0]][now[0][1]]) > now[1]:
            # if now[0] not in now[2]:
            #     now[2].append(now[0])
            now[2][now[0][0]][now[0][1]] = '#'
            now[1] = e

        if now[1] <= 0:
            continue

        # now[2][now[0][0]][now[0][1]] = '#'
        for d in directions:

            if 0 <= (h_ := now[0][0] + d[0]) < H and 0 <= (w_ := now[0][1] + d[1]) < W:
                if now[2][h_][w_] != "#":
                    queue.append([(h_, w_), now[1] - 1, now[2].copy()])

    print('No')


if __name__ == '__main__':
    main()
