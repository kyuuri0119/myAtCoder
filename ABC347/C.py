
def main():
    N, A, B =  map(int,input().split())

    D = set(map(lambda x: int(x)%(A+B), input().split()))

    if len(D)>1:
        if max(D) - min(D) < A:
            print('Yes')
        else:
            print('No')
    else:
        print('Yes')

    # for t in range(A):
    #
    #     res = True
    #     for d in D:
    #         if not (0 < (d+t)%(A+B) < A+1):
    #             res = False
    #             break
    #     if res:
    #         print('Yes')
    #         return
    #
    # print('No')


if __name__ == '__main__':
    main()

