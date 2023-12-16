import math
from copy import copy


def main():
    H,W = map(int, input().split())
    A = []
    B = []
    sumA = 0
    sumB = 0
    for i in range(H):
        l_a = list(map(int, input().split()))
        sumA += sum(l_a)
        A.append(l_a)
    for i in range(H):
        l_b = list(map(int, input().split()))
        sumB += sum(l_b)
        B.append(l_b)

    M, has_diff = get_diff_matrix(A,B,H,W)

    # import numpy as np
    # print(np.matrix(M))

    if sumA != sumB:
        print(-1)
        return

    c = 0
    while c< math.factorial(H) + math.factorial(W):
        for i in range(H):
            need_break = False
            for j in range(W):
                if M[i][j]!=0:
                    # c+=1
                    diff_h, diff_w = calc_dist(i,j,A,B)

                    c+=abs(diff_h)+abs(diff_w)

                    if diff_h!=0:
                        i_ = min(i,i+diff_h)
                        for _ in range(abs(diff_h)):
                            for w in range(W):
                                A[i_][w],A[i_+1][w] = A[i_+1][w], copy(A[i_][w])
                            # A[i_],A[i_+1] = A[i_+1], A[i]

                            # M[i_],M[i_+1] = M[i_+1], M[i]
                            i_+= 1

                    if diff_w!=0:
                        j_ = min(j, j+diff_w)
                        for _ in range(abs(diff_w)):
                            for h in range(H):
                                A[h][j_], A[h][j_+1] = A[h][j_+1], copy(A[h][j_])
                                # M[h][j_], M[h][j_+1] = M[h][j_+1], M[h][j_]
                            j_ +=1

                    if diff_h or diff_w:
                        need_break = True
                        break
            if need_break:
                break


        M, has_diff = get_diff_matrix(A,B,H,W)
        # print(np.matrix(M))

        if not has_diff:
            print(c)
            return


    print(-1)

def get_diff_matrix(A,B, H, W):
    M_ = []
    has_diff = False
    for i in range(H):
        diff= []
        for w in range(W):
            m = A[i][w] - B[i][w]
            diff.append(m)
            if m!=0:
                has_diff = True
        M_.append(diff)
    return M_, has_diff
def calc_dist(i, j, A, B):
    target = A[i][j]
    for h in range(len(A)):
        for w in range(len(A[0])):

            if B[h][w] == target:
                return h-i, w-j
    return 0, 0

if __name__ == '__main__':
    main()