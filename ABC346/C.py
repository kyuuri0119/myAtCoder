
def main():
    N, K =  map(int,input().split())
    A = set(map(int, input().split()))

    sum_a = 0
    for a in A:
        if a<=K:
            sum_a+=a

    sum_k = (K*(K+1))//2

    print(sum_k-sum_a)


if __name__ == '__main__':
    main()

