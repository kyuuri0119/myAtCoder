def main():
    N = int(input())

    item = [0, 2, 4, 6, 8]

    x = N-1
    idx_l = []
    while x>0:

        idx_l.append(x%5)
        x = x//5
        # print(x, idx_l)

    # idx_l.append(x%5)
    # idx_l.append(x//5)
    # print(x, idx_l)

    res = ''

    for i in reversed(idx_l):
        res+=f'{item[i]}'

    if res=='0' or res=='':
        print(0)
    else:
        print(res)


if __name__ == '__main__':
    main()