def main():
    N = int(input())

    G = []

    P = []

    for i in range(N):
        S = input()
        G.append(list(S))

        if 'P' in S:
            idx = S.index('P')
            P.append([i,idx])
            G[i][idx] = '.'

    print(G)
    print(P)

    def move_player(player, move):
        if not(0 < player[0] + move[0] < N):
            return [*player]
        elif not(0 < player[1] + move[1] < N):
            return [*player]

        moved = [player[0] + move[0], player[1] + move[1]]
        if G[moved[0]][moved[1]]=='#':
            return [*player]

        return moved


    def turn(angle,p1, p2):

        next_pos = [0,0]
        if angle%4 == 0:
            next_pos[0] -= 1
        elif angle%4 == 1:
            next_pos[1] += 1
        elif angle%4 ==2:
            next_pos[0] +=1
        elif angle%4 == 3:
            next_pos[1] -=1

        next_p1 = move_player(p1, next_pos)
        next_p2 = move_player(p2, next_pos)

        return  next_p1, next_p2

    result = -1
    count = 0
    p1s = [P[0]]
    p2s = [P[1]]
    while count < (N+1)*2:
        count+=1
        _p1s = []
        _p2s = []
        for a in range(4):
            if count == 1:
                p1 = p1s[0]
                p2 = p2s[0]
                _p1, _p2 = turn(a, p1, p2)
                if _p1 == _p2:
                    result = count
                    break

                _p1s.append(_p1)
                _p2s.append(_p2)
            else:
                for p in range(len(p1s)):
                    p1 = p1s[p]
                    p2 = p2s[p]
                    _p1, _p2 = turn(a,  p1, p2)
                    if _p1 == _p2:
                        result = count
                        break

                    _p1s.append(_p1)
                    _p2s.append(_p2)
            if result>0:
                break
        if result>0:
            break

        # print(count, _p1s, _p2s)

        p1s = _p1s
        p2s = _p2s


    if result !=  (N+1)*2:
        print(result)
    else:
        print(-1)


if __name__ == '__main__':
    main()