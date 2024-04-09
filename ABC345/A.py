
def main():
    S= input()


    if S[0]!='<' or S[-1]!='>':
        print('No')
        return

    for s in S[1:-1]:
        if s !='=':
            print('No')
            return

    print('Yes')


if __name__ == '__main__':
    main()