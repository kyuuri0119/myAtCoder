import math
import sys
from functools import cache

sys.setrecursionlimit(20000000)

def main():
    H,W,N = map(int, input().split())
    T = input()
    G = []
    res = 0

    for i in range(H):
        s=input()
        G.append(list(s))


    def move(pos, c):
        if c == 'R':
            pos[1]+=1
        elif c == 'L':
            pos[1]-=1
        elif c == 'U':
            pos[0]-=1
        elif c == 'D':
            pos[0]+=1

        return pos

    def dfs(i, j, t):
        # print(i, j ,t)
        if t==N:
            return True

        next_pos = move([i,j], T[t])
        if G[next_pos[0]][next_pos[1]] == '.':
            return dfs(next_pos[0], next_pos[1], t+1)
        else:
            return False


    for i_ in range(1,H-1):
        for j_ in range(1,W-1):
            if G[i_][j_] == ".":

                if dfs(i_, j_, 0):
                    # print(i_, j_)
                    res += 1

    print(res)

def main2():
    H,W,N = map(int, input().split())
    T = input()
    G = []
    res = 0

    for i in range(H):
        s=input()
        G.append(list(s))

    def move(pos, c):
        if c == 'R':
            pos[1]+=1
        elif c == 'L':
            pos[1]-=1
        elif c == 'U':
            pos[0]-=1
        elif c == 'D':
            pos[0]+=1

        return pos

    pos = [0, 0]
    m_move = [0, 0, 0, 0] # LRUD
    for t in T:
        pos = move(pos, t)
        m_move[0] = min(pos[1], m_move[0])
        m_move[1] = max(pos[1], m_move[1])
        m_move[2] = min(pos[0], m_move[2])
        m_move[3] = max(pos[0], m_move[3])

    # print(m_move)

    def dfs(i, j, t):
        # print(i, j ,t)
        if t==N:
            return True

        next_pos = move([i,j], T[t])
        if G[next_pos[0]][next_pos[1]] == '.':
            return dfs(next_pos[0], next_pos[1], t+1)
        else:
            return False


    for i_ in range(-m_move[2],H-m_move[3]):
        for j_ in range(-m_move[0],W-m_move[1]):
            if G[i_][j_] == ".":

                # print(i_, j_, G[i_+pos[0]][j_+pos[1]])
                if G[i_+pos[0]][j_+pos[1]] == '.':
                    # print(i_, j_)
                    if dfs(i_, j_, 0):
                        res += 1

    print(res)
if __name__ == '__main__':
    # main()

    main2()
