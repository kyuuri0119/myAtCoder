def main():
    N = int(input())

    A = list(map(int, input().split()))

    for i in range(N-1):
        s, t = map(int, input().split())
        if A[i] >= s:
            x = A[i]//s
            A[i] -= s*x
            A[i+1] += t*x

    print(A[-1])

if __name__ == '__main__':
    main()