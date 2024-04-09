def main():
    W, B =  map(int,input().split())

    S = 'wbwbwwbwbwbw'*18

    for i in range(13):
        s = S[i:i+W+B]

        if s.count('w') == W and s.count('b')==B:
            print('Yes')
            return
    print('No')



if __name__ == '__main__':
    main()