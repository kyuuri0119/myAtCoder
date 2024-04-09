import collections

def main():
    H,W, M = map(int,input().split())

    # 残塗れる箇所
    r_row = W
    r_col = H

    c_row = collections.defaultdict(int)
    c_col = collections.defaultdict(int)

    color = collections.defaultdict(int)
    color[0] = H*W

    tasks = [list(map(int, input().split())) for i in range(M)]

    # print(tasks)

    for t in reversed(tasks):
        p = -1 if t[2]==0 else t[2]

        if t[0] == 1:
            if c_row[t[1]-1] == 0:
                if r_row>0:
                    color[p] = r_row
                    c_row[t[1]-1] = p
                if p>0:
                    color[0]-=r_row
                r_col -= 1

        else:
            if c_col[t[1]-1] == 0:
                if r_col>0:
                    color[p] = r_col
                    c_col[t[1]-1] = p
                if p>0:
                    color[0]-=r_col
                r_row -= 1

        # print(color)

    k = len(color.keys())
    if -1 in color.keys():
        k-=1
    if color[0]==0:
        k-=1
        del color[0]
    print(k)

    for k, v in sorted(color.items(), key=lambda x:x[0]):
        if k>=0 and v >= 0:
            print(k, v)





if __name__ == '__main__':
    main()