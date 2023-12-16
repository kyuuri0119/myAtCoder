def main():
    H, W = map(int, input().split())
    G = [list(input()) for i in range(H)]


    r = 0
    br = 0
    c = 0
    bc = 0

    hist = {}
    get_loop = 0

    while 0 <= r < H and 0 <= c < W:
        if hist.get(f'{r},{c}'):
            get_loop = 1
            break
        else:
            hist[f'{r},{c}'] = 1
        br = r
        bc = c
        g = G[r][c]
        if g == 'U':
            r-=1
        elif g == 'D':
            r += 1
        elif g == 'L':
            c -=1
        elif g == 'R':
            c += 1

    if get_loop:
        print(-1)
    else:
        print(br+1, bc+1)

if __name__ == '__main__':
    main()
