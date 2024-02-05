def main():
    N = int(input())

    c = 0
    n = 0
    sum_n_d = {f"{i}": i for i in range(11)}
    while n < N:

        n += 1

        ns = f"{n}"
        if n > 10 and (m := sum_n_d.get(ns[1:])):
            sum_n = m + int(ns[0])
            sum_n_d[ns] = sum_n
        # elif n > 10 and (m := sum_n_d.get(ns[:-1])):
        #     sum_n = m + int(ns[-1])
        #     sum_n_d[ns] = sum_n
        elif m:=sum_n_d.get(ns):
            sum_n = m
        else:
            sum_n = sum(map(int, list(f"{n}")))
            sum_n_d[ns] = sum_n

        if n % sum_n == 0:
            c+=1

            # print(sum_n, n, c)

    print(c)

def after():
    N = int(input())

    pat = [i for i in range(1, 9*14)]

    dp = [[] for p in range(len(pat))]
    for p in pat:

        while


if __name__ == '__main__':
    main()