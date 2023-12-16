from collections import defaultdict


def main():
    N = int(input())
    S = input()

    d = defaultdict(int)

    count = 1
    d[S[0]] = 1
    for idx, s in enumerate(S):
        if idx == 0:
            continue

        if s == S[idx-1]:
            count += 1
        else:
            if d[S[idx-1]] < count:
                d[S[idx-1]]=count
            count = 1

        if idx == N-1:
            if d[S[idx-1]] < count:
                d[S[idx-1]]=count

    print(sum(d.values()))


if __name__ == '__main__':
    main()