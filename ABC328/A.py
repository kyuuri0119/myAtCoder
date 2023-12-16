def main():
    N, X = map(int, input().split())
    SL = map(int, input().split())

    r = 0
    for s in SL:
        if s <= X:
            r+= s

    print(r)



if __name__ == '__main__':
    main()