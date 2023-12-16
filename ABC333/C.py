import itertools


def main():
    N = int(input())

    def Base_10_to_n(X, n):
        if (int(X / n)):
            return Base_10_to_n(int(X / n), n) + str(X % n)
        return str(X % n)

    pat = [3]
    c = 3
    r = 1
    while r < N:
        c+=1
        tri = [int(v) for v in Base_10_to_n(c, 4)]
        if sum(tri) == 3:
            # print(tri)
            pat = tri
            r+=1

    l = [int(v) for v in reversed(pat)]
    # print(l)
    res = 0
    for i, x in enumerate(l):
        rp = int('1'*(i+1))
        res += rp*x

    print(res)

def other():
    N = int(input())

    pat = [int('1'*i) for i in range(1,15)]

    comb = itertools.combinations_with_replacement(pat, 3)

    res_pat = sorted(list({sum(c) for c in comb}))

    print(res_pat[N-1])





if __name__ == '__main__':
    # main()
    other()