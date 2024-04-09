import string


def main():
    N = int(input())

    S = input()

    Q = int(input())

    setS_l =list(set(list(S)))
    setS = ''.join(setS_l)

    for i in range(Q):
        c, d = input().split()

        setS = setS.replace(c, d)

    r_d = {setS_l[i]: setS[i] for i in range(len(setS_l))}

    S_ = list(S)
    for i in range(len(S)):
        S_[i] = r_d[S_[i]]

    print("".join(S_))

if __name__ == '__main__':
    main()