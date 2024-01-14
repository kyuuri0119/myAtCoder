
def main():
    N,Q = map(int, input().split())

    dragon = [[i, 0] for i in reversed(range(1,N+1))]

    def move_head(c):
        head = dragon[-1].copy()
        if c == 'R':
            head[0]+=1

        elif c == 'L':
            head[0]-=1
        elif c == 'U':
            head[1]+=1
        elif c == 'D':
            head[1]-=1

        dragon.append(head)

    for i in range(Q):
        t, q = input().split()

        if t == '1':
            move_head(q)
        else:
            print(*dragon[-1*int(q)])


if __name__ == '__main__':
    main()