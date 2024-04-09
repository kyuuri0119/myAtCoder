import collections

def main():
    N=int(input())
    A = list(map(int,input().split()))
    Q=int(input())

    ad = {A[i]: [A[i-1], A[i+1]] for i in range(1,N-1)}
    ad[0] = [0, A[0]]

    if len(A)>1:
        ad[A[0]]=[0, A[1]]
        ad[A[-1]]=[A[-2], -1]
    else:
        ad[A[0]]=[0, -1]
    ad[-1] = [A[-1], -1]

    for t in range(Q):
        q = list(map(int,input().split()))

        if q[0] == 1:

            bef = q[1]
            aft = ad[q[1]][1]
            ad[q[2]]= [bef,aft]

            ad[bef][1] = q[2]
            ad[aft][0] = q[2]

        else:

            bef, aft = ad[q[1]]

            ad[bef][1] = aft
            ad[aft][0] = bef
            del ad[q[1]]

    res = []
    s = ad[0]
    while True:
        if s[-1]==-1:
            break
        res.append(s[1])
        s=ad[s[1]]

    print(*res)



if __name__ == '__main__':
    main()