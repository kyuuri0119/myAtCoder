def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))

    PQR = P + Q + R

    get_q = 0

    for x in range(0, N - 2):
        for w in range(x + 3, N+1):
            pqr = sum(A[x:w])
            if pqr == PQR:
                for y in range(x + 1, w - 1):
                    p = sum(A[x:y])
                    if p == P:
                        for z in range(y + 1, w):
                            q = sum(A[y:z])
                            if q == Q:
                                get_q = 1
                                break
                            elif q > Q:
                                break
                    elif p > P or get_q:
                        break
            if pqr > PQR:
                break
            if get_q:
                break
        if get_q:
            break


    if get_q:
        print('Yes')
    else:
        print('No')


def main2():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))

    sum_a = A[0]
    acc_list = [A[0]]
    for a in A[1:]:
        sum_a+=a
        acc_list.append(sum_a)
    acc = set(acc_list)
    print(acc_list)
    print(acc)


    has_result = False

    for x in range(0, N):
        if acc_list[x]+P in acc:
            if acc_list[x]+P+Q in acc:
                if acc_list[x]+P+Q+R in acc:
                    has_result = True
                    break

    if has_result:
        print('Yes')
    else:
        print('No')



if __name__ == '__main__':
    main2()
