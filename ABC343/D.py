import collections

def main():
    N, T= map(int,input().split())

    p = [0]*N

    p_p = collections.defaultdict(set)
    p_p[0]={i+1 for i in range(N)}

    for t in range(T):
        A, B = map(int, input().split())

        bef = p[A-1]
        p[A-1] += B
        p_p[bef].remove(A)
        if not p_p[bef]:
            del p_p[bef]
        p_p[p[A-1]].add(A)

        print(len(p_p.keys()))




if __name__ == '__main__':
    main()