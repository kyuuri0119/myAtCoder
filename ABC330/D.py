import math


def main():
    N = int(input())
    S = []
    for i in range(N):
        s = input()
        S.append(list(s))
    # print(S)

    ans = 0

    for r in range(0,N):
        target_c = []
        for i in range(N):
            if S[r][i] == 'o':
                target_c.append(i)
        if len(target_c) < 2:
            continue

        for c in target_c:
            c_num = 0
            for i in range(0, N):
                if i == r:
                    continue

                if S[i][c] == 'o':
                    c_num+=1
            # print(ans, c_num, (len(target_c)-1))
            ans += c_num * (len(target_c)-1)

    print(ans)

def after():
    N = int(input())
    S = []

    r_count = [0]*N
    c_count = [0]*N

    ans = 0

    for r in range(N):
        s = input()
        S.append(list(s))

        for c in range(N):
            if S[r][c] == 'o':
                r_count[r] += 1
                c_count[c] += 1

    for r in range(N):
        for c in range(N):
            if S[r][c] == 'o':
                ans += (r_count[r]-1) * (c_count[c] -1)

    print(ans)


if __name__ == '__main__':
    after()