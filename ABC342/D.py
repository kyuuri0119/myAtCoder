from functools import cache
from math import sqrt


def main():
    N = int(input())

    A = list(map(int, input().split()))



    pat = {i * i for i in range(1, (2 * 10**5)+1) }
    res = 0
    for i in range(N-1):
        for j in range(i+1, N):
            # print(A[i]*A[j])
            if A[i]*A[j] in pat:
                res+=1
            # if is_ans(A[i]*A[j]):
            #     res+=1

    print(res)



if __name__ == '__main__':
    main()