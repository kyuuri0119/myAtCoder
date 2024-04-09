def main():
    N= int(input())

    res = ''
    while len(res)<=2*N:
        if len(res)%2 == 0:
            res+="1"
        else:
            res+="0"

    print(res)


if __name__ == '__main__':
    main()