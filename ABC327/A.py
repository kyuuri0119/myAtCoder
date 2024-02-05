def main():
    N = int(input())
    S = input()

    S = '_' + S
    for i in range(N):
        if S[i:i+2] == 'ab' or S[i:i+2] == 'ba':
            print('Yes')
            return

    print('No')

if __name__ == '__main__':
    main()
