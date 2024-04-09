import itertools
import sys

sys.setrecursionlimit(1_000_000_000)


def main():
    N,H,W = map(int,input().split())

    tiles = []
    for i in range(N):
        a, b =map(int, input().split())

        tiles.append((a, b))

    G = [[0]*W for i in range(H)]
    G_ = G.copy()

    unused = [i for i in range(N)]
    used = []

    pat = list(itertools.permutations(set(unused)))


    for p in pat:
        nex_i = 0
        nex_j = 0

        unused = list(p)
        used = []

        max_w = W-nex_i
        max_h = H-nex_j

        while True:
            if max_w == 0 and max_h == 0:
                print('Yes')
                return

            for uui in unused:

                tile = tiles[uui]
                if tile[0] < max_w and tile[1] < max_h:
                    used.append(uui)
                    unused.remove(uui)
                    # for i in range(nex_i, nex_i+tile[0]):
                    #     for j in range(nex_j, nex_j+tile[1]):
                    #         G_[i][j] = 1

                    nex_i += tile[0]
                    if nex_i != max_w:
                        nex_j += 0
                    else:
                        nex_j +=
                    break

                elif tile[1] < max_w and tile[0] < max_h:
                    used.append(uui)
                    unused.remove(uui)
                    # for i in range(nex_i, nex_i+tile[1]):
                    #     for j in range(nex_j, nex_j+tile[0]):
                    #         G_[i][j] = 1

                    nex_i += tile[1]
                    nex_j += tile[0]
                    break


            print(used, p, unused)

    print('No')






if __name__ == '__main__':
    main()