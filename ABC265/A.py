def main():
    X, Y, N = map(int, input().split())
    y = N//3*Y + N%3 * X
    x = X*N

    print(min(y,x))


if __name__ == '__main__':
    main()