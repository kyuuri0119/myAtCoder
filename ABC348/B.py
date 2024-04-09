from collections import defaultdict


def main():
    N = int(input())
    p = []
    for i in range(N):
        x, y = map(int, input().split())
        p.append((x, y))

    dist = {i: [0, 0] for i in range(N)}
    for i in range(N - 1):
        for j in range(i + 1, N):
            d = pow(p[i][0] - p[j][0], 2) + pow(p[i][1] - p[j][1], 2)

            if dist[i][1] < d:
                dist[i][0] = j
                dist[i][1] = d

            if dist[j][1] < d:
                dist[j][0] = i
                dist[j][1] = d

    for i in range(N):
        print(dist[i][0]+1)

if __name__ == '__main__':
    main()
