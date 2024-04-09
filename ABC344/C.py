
def main():
    N = input()
    A = set(map(int, input().split()))
    M = input()
    B = set(map(int, input().split()))
    L = input()
    C = set(map(int, input().split()))
    Q = input()
    X = list(map(int, input().split()))

    res = {a+b+c for a in A for b in B for c in C}

    for x in X:
        if x in res:
            print('Yes')
        else:
            print('No')



if __name__ == '__main__':
    main()