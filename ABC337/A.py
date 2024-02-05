def main():
    N = int(input())

    t = 0
    a = 0
    for i in range(N):
        X, Y = map(int,input().split())

        t+=X
        a+=Y

    if t>a :
        print('Takahashi')
    elif a>t :
        print('Aoki')
    else:
        print('Draw')




if __name__ == '__main__':
    main()