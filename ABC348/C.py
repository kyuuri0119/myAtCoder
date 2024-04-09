from collections import defaultdict


def main():
    N = int(input())
    b = defaultdict(lambda: 1_000_000_001)

    for i in range(N):
        a, c = map(int, input().split())
        b[c] = min(b[c], a)

    print(max(b.values()))



if __name__ == '__main__':
    main()

