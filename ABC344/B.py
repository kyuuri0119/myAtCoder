def main():

    A = []
    while True:

        a = int(input())
        A.append(a)

        if a == 0:
            break

    for a in reversed(A):
        print(a)



if __name__ == '__main__':
    main()