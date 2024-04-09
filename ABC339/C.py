def main():
    N = int(input())
    A = list(map(int, input().split()))

    min_h = 0
    max_h = 0
    now = 0

    for a in A:
        now += a
        min_h = min(min_h, now)
        max_h = max(max_h, now)
        # print(now, min_h, max_h)
    # last = now
    # now = min_h

    if min_h < 0:
        now+= abs(min_h)

    # res = min(now, max_h)
    print(now)





if __name__ == '__main__':
    main()