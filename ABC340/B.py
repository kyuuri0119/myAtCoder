def main():
    Q = int(input())

    A = []

    for i in range(Q):
        q1, q2 = input().split()
        if q1 == '1':
            A.append(q2)
        else:
            print(A[-1*int(q2)])


if __name__ == '__main__':
    main()