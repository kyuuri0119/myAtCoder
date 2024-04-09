
def main():
    S= input()

    if S[0]=='|':
        S = ' '+S
    if S[-1]=='|':
        S = S+' '

    s = S.split('|')
    print((s[0]+s[2]).strip())


if __name__ == '__main__':
    main()