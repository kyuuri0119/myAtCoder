def main():

    N, Q = list(map(int, input().split()))
    S = str(input())

    # S_target_idx = [1 if S[i] == S[i+1] else 0 for i in range(min_l-1,max(R)-1)]
    S_target_idx = [0]
    sum = 0
    for i in range(N-1):
        sum = S_target_idx[i] + (1 if S[i] == S[i+1] else 0)
        S_target_idx.append(sum)

    print(S_target_idx)

    for q in range(1, Q+1):
        l,r = list(map(int, input().split()))
        # print(S_target_idx[l-1:r-1])
        # print(L[q-1] - min_l ,R[q-1] - min_l)
        # print((S[L[q-1] - min_l:R[q-1] - min_l]))
        print(S_target_idx[r-1] - S_target_idx[l-1])

if __name__ == '__main__':
    main()