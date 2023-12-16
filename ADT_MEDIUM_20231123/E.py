def main():
    N, M = map(int,(input().split()))
    S = list(map(str, input().split()))
    T = set(map(str, input().split()))

    for s in S:

        print('Yes' if s in T else 'No')


if __name__ == '__main__':
    main()