def main():
    H,W,N = map(int,input().split())

    g = [['.' for w in range(W)] for h in range(H)]

    now = [0,0] # gyou, retu

    angle = 0
    for i in range(N):

        if g[now[0]][now[1]] == '.':
            g[now[0]][now[1]] = '#'
            angle+=1
        else:
            g[now[0]][now[1]] = '.'
            angle-=1

        if angle%4 == 0:
            now[0] -= 1
        elif angle%4 == 1:
            now[1] += 1
        elif angle%4 ==2:
            now[0] +=1
        elif angle%4 == 3:
            now[1] -=1

        if now[0] == -1:
            now[0] = H-1
        elif now[0] == H:
            now[0] = 0

        if now[1] == -1:
            now[1] = W-1
        elif now[1] == W:
            now[1] = 0

    for i in range(H):
        print("".join(g[i]))


if __name__ == '__main__':
    main()