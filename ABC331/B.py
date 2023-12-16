import math


def main():
    N, S, M, L = map(int, input().split())

    s = N//6 + 1
    m = N //8 +1
    l = N//12 +1


    res = math.inf

    for l_ in range(l+1):
        for m_ in range(m+1):
            for s_ in range(s+1):
                if 6*s_+8*m_+12*l_ >= N:
                    res = min(res, S*s_ + M*m_ + L*l_)

    print(res)


if __name__ == '__main__':
    main()