
def main():
    H, W = map(int, input().split())
    A = []
    sum_row = []
    sum_col = [0]* W

    for _ in range(H):
        row = list(map(int, input().split()))
        A.append(row)
        sum_row.append(sum(row))

        for i, r in enumerate(row):
            sum_col[i] += r

    for h in range(H):
        row = []
        for w in range(W):
            row.append(sum_row[h]+sum_col[w] - A[h][w])

        print(*row)



if __name__ == '__main__':
    main()