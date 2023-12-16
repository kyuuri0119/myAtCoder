
def main():
    N, L, R = map(int,input().split())
    A = list(map(int,input().split()))

    ans = []
    for i, a in enumerate(A):
        if a<=L:
            ans.append(str(L))

        elif a>=R:
            ans.append(str(R))

        else:
            ans.append(str(a))

    print(" ".join(ans))


if __name__ == '__main__':
    main()