import sys

sys.setrecursionlimit(10 ** 9)

def main():
    N = int(input())

    tree = [[] for _ in range(N)]

    for i in range(N-1):
        u, v = map(int, input().split())

        tree[u-1].append(v-1)
        tree[v-1].append(u-1)
    # print(tree)

    results = []
    counts = []

    def bfs(start, parent, count):
        if len(tree[start])>1:
            c = 0
            for next_n in tree[start]:
                if next_n == parent:
                    continue

                c += bfs(next_n, start, count)

            count+=c

        return count + 1

    if len(tree[0]) == 1:
        print(1)
    else:
        sc = 0
        for n in tree[0]:
            sub_res = bfs(n, 0, 0)
            counts.append(sub_res) # root分+1
            sc += sub_res

        for i in range(len(counts)):
            counts[i] = sc- counts[i] +1
            # results.append(sc-counts[i]+1)
        # print(results)
        print(min(counts))


if __name__ == '__main__':

    main()