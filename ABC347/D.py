import itertools
import sys

sys.setrecursionlimit(1_000_000_000)


def main():
    a, b, C =  map(int,input().split())

    max_bit = min(max(max(a*2, b*2), C.bit_count()*2), 60)

    Xs = list(itertools.combinations(range(0, max_bit), a))
    Ys = list(itertools.combinations(range(0, max_bit), b))

    # print(list(Xs))
    # print(Ys)

    for xs in Xs:
        for ys in Ys:
            x = ['0']*60
            y = ['0']*60
            for p in xs:
                x[-p-1] = '1'
            for p in ys:
                y[-p-1] = '1'

            x = ''.join(x)
            y = ''.join(y)
            # print(x, y, int(x, 2)^int(y, 2),  (int(x, 2) ^ int(y, 2)) == C)
            if (int(x, 2) ^ int(y, 2)) == C:
                print(int(x, 2), int(y, 2))
                return

    print('No')










if __name__ == '__main__':
    main()