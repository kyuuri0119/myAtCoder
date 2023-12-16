def main():
    K,G,M = map(int, input().split())

    g = 0
    m = 0

    for k in range(K):
        if g == G:
            g=0

        elif m == 0:
            m =M

        else:
            diff_g = G-g
            if m - diff_g>=0:
                m -= diff_g
                g += diff_g
            else:
                g += m
                m = 0

    print(f'{g} {m}')

if __name__ == '__main__':
    main()