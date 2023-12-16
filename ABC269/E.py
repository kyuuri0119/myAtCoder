def main():
    N = int(input())

    A = 1
    B = floor_div(N, 2)
    C = 1
    D = N

    target = 'i'

    while True:
        print('?', A, B, C, D)

        T = int(input())
        if T == -1:
            return

        if T == 0 and target == 'j':
            print('!', result_i, C)
            break

        if T == 0 and target == 'i':
            result_i = A
            A = 1
            B = N
            target = 'j'

        if target == 'i':
            l = A
            r = B
        else:
            l = C
            r = D

        d = r - l + 1

        if T == d and l != r:
            tmpl = l
            l = r
            r = r + (r - tmpl)
            if r > N:
                r = N
        elif T < d:
            r = r - floor_div(r - l, 2)
        else:
            l += 1
            r += 1

        if target == 'i':
            A = l
            B = r
        else:
            C = l
            D = r


def floor_div(a, b):
    return -(-a // b)


if __name__ == '__main__':
    main()
