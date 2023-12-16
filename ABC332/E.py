def main():
    N, D = map(int, input().split())
    W = list(map(int, input().split()))

    if D==N:
        print(calc_v(W))
        return




def calc_v(dl: list):
    mean = sum(dl)/len(dl)
    res = 0
    for i in range(len(dl)):
        res += pow(dl[i]-mean, 2)

    return res / len(dl)

if __name__ == '__main__':
    main()