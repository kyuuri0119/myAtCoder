import collections

def main():
    N, Q= map(int,input().split())
    A = list(map(int,input().split()))

    # p = [0]*N

    p_p = collections.defaultdict(set)
    for i, a in enumerate(A):
        p_p[a].add(i+1)

    for t in range(Q):
        q, x, y = map(int, input().split())
        if q == 1:

            bef = A[x-1]
            A[x-1] = y
            p_p[bef].remove(x)
            if not p_p[bef]:
                del p_p[bef]
            p_p[A[x-1]].add(x)

        else:
            keys = {k for k in A[x-1:y]}
            if len(keys)>1:
                keys.remove(max(keys))
                res = p_p[max(keys)]

                print(len({i for i in res if x<=i<=y}))
            else:
                print(0)




if __name__ == '__main__':
    main()