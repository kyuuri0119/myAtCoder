def main():
    N = int(input())
    A = sorted(list(map(int, input().split())), reverse=True)

    max_a = max(A)
    for a in A:
        if a != max_a:
            print(a)
            break


if __name__ == '__main__':
    main()