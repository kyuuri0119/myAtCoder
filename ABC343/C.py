import string


def main():
    N = input()

    # target = [pow(x, 3) for x in range(max(2, min(int(pow(int(N), 1/3))+1,1_000_001)))]
    target = [pow(x, 3) for x in range(1_000_001) if pow(x, 3)<=int(N)]

    for t in reversed(target):
        s = list(str(t))
        if len(s) == 1:
            print(t)
            return

        if all(s[i]==s[-i-1] for i in range(len(s)//2+1)):
            print(t)
            return




if __name__ == '__main__':
    main()