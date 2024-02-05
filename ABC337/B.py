def main():
    S = input()

    S = S.lstrip('A')
    S = S.lstrip('B')
    S = S.lstrip('C')

    # print(S)

    if S == '':
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()