def main():
    M, D = map(int,input().split())
    y, m, d = map(int,input().split())

    d +=1
    if d == D+1:
        d=1
        m+=1
    if m == M+1:
        m = 1
        y+=1

    print(f'{y} {m} {d}')


if __name__ == '__main__':
    main()