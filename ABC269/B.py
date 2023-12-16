def main():
    s = []
    A = 0
    B = 0
    C = 0
    D = 0

    for i in range(10):
        s.append(input())

    for i in range(10):
        if A == 0 and '#' in s[i]:
            A = i+1
            D = s[i].rfind('#')+1

        if A != 0 and '#' in s[i]:
            B = i + 1
            C = s[i].find('#')+1



    print(A, B)
    print(C, D)






if __name__ == '__main__':
    main()
