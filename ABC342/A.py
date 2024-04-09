from collections import defaultdict


def main():
    S= input()

    bef = S[0]
    res = 1
    for s in S:
        if s != bef:
            if res == len(S):
                print(res)
                return
            if S[res] !=s:
                print(res)
                return
        bef = s
        res+=1
    print(1)


if __name__ == '__main__':
    main()