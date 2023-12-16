from collections import defaultdict


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    d = defaultdict(int)
    max_p = (0, 0)
    for a in A:
        d[a] += 1
        if d[a] > max_p[1]:
            print(a)
            max_p = (a, d[a])
        elif d[a] == max_p[1]:
            target = min(max_p[0], a)
            print(target)
            max_p = (target, d[target])
        else:
            print(max_p[0])

if __name__ == '__main__':
    main()