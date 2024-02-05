def main():
    H, W, K = map(int, input().split())

    G = []

    res = []
    res_h = []
    res_w = []
    p_w = [0]*W
    c_c = [0]*W
    for h in range(H):
        l = list(input())
        c = 0
        p = 0
        for w, s in enumerate(l):

            if s == 'x':
                c=0
                p=0
                c_c[w]=0
                p_w[w] = 0
            else:
                c+=1
                c_c[w]+=1

                if s == '.':
                    p += 1
                    p_w[w] += 1

            if c >= K:
                if w-K>=0 and l[w-K] == '.':
                    p -= 1
                res_h.append((h, w-K+1, p))
                res.append(p)
            if c_c[w]>=K:
                if h-K>=0 and G[h-K][w] == '.':
                    p_w[w] -= 1
                res_w.append((h-K+1, w, p_w[w]))
                res.append(p_w[w])
        G.append(l)

    # for i in range(H):
    #     print(G[i])

    # min_res = K+1
    # if res_h:
    #     for h, start_w in res_h:
    #         c = 0
    #         for w in range(start_w, start_w+K):
    #             if G[h][w] == '.':
    #                 c+=1
    #                 if min_res < c:
    #                     break
    #
    #         # if c < min_res:
    #         #     print(h, w)
    #         min_res = min(c, min_res)
    #
    #
    # if res_w:
    #     for start_h, w in res_w:
    #         c = 0
    #         for h in range(start_h, start_h+K):
    #             if G[h][w] == '.':
    #                 c+=1
    #                 if min_res < c:
    #                     break
    #
    #         # if c < min_res:
    #         #     print(h, w)
    #         min_res = min(c, min_res)
    #
    #
    # if min_res < K+1:
    #     print(min_res)
    # else:
    #     print(-1)

    if res:
        print(min(res))
    else:
        print(-1)

if __name__ == '__main__':
    main()