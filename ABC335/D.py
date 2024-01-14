import itertools


def main():
    N = int(input())

    G = [['' for i in range(N)] for i in range(N)]

    count = 2
    G[0][0]='1'
    G[(N+1)//2 -1][(N+1)//2-1] = 'T'
    direction = 'R'
    target = [0, 0]
    while count < N * N:
        if direction == 'R':
            if 0 <= target[0] + 1 < N and G[target[1]][target[0] + 1] == '':
                target[0] += 1
            else:
                direction = 'U'
                continue
        elif direction == 'L':
            if 0 <= target[0] - 1 < N and G[target[1]][target[0] - 1] == '':
                target[0] -= 1
            else:
                direction = 'D'
                continue
        elif direction == 'U':
            if 0 <= target[1] + 1 < N and G[target[1] + 1][target[0]] == '':
                target[1] += 1
            else:
                direction = 'L'
                continue
        elif direction == 'D':
            if 0 <= target[1] - 1 < N and G[target[1] - 1][target[0]] == '':
                target[1] -= 1
            else:
                direction = 'R'
                continue

        G[target[1]][target[0]] = str(count)
        count += 1

    for i in reversed(range(N)):
        print(*G[i])


if __name__ == '__main__':
    main()
