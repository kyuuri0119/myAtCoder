
def main():
    B = int(input())

    A = 0
    AA = 0
    while AA<B:
        A+=1
        AA = pow(A,A)
        if AA == B:
            print(A)
            return

    print(-1)

if __name__ == '__main__':
    main()