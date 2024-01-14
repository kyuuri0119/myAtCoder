import sys

sys.setrecursionlimit(10 ** 9)

def main():
    N, M = map(int, input().split())

    A = list(map(int, input().split()))

    G = {}

    for m in range(M):
        u, v = map(int, input().split())
        if not G.get(u):
            G[u]=set()
        if not G.get(v):
            G[v]=set()

        G[u].add(v)
        G[v].add(u)

    results = [0]

    def bfs(current = 1, visited=[1]):
        if current == N:

            results.append(len(set([A[u-1] for u in visited])))
            return visited

        nexts = list(G[current] - set(visited))

        if nexts:
            for c in nexts:
                if A[current-1] <= A[c-1]:
                    bfs(c, [*visited, c])
        #         else:
        #             return []
        # else:
        #     return visited

    bfs(1,[1])

    # print(paths)

    # def check_path(path):
    #     old = 0
    #     points = set()
    #     for u in path:
    #         if old <= A[u-1]:
    #             old = A[u-1]
    #             points.add(A[u-1])
    #         else:
    #             return 0
    #     return len(points)

    # result = 0
    # for path in sorted(paths, key=len, reverse=True):
    #     if len(path) < result:
    #         break
    #     point = len(path)
    #     result = max(result, point)

    print(max(results))

if __name__ == '__main__':
    main()