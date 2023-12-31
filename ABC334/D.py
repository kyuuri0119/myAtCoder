import sys
import bisect

sys.setrecursionlimit(10 ** 9)

def main():
    N,Q = map(int, input().split())
    R = list(map(int, input().split()))

    sorted_R = sorted(R)

    memo = [(0,0)]


    for q_i, i in enumerate(range(Q)):
        q = int(input())
        origin_q = q
        res = 0
        r_idx = 0

        for j in reversed(range(len(memo))):
            _r, _r_idx = memo[j]
            if q >= _r:
                q -= _r
                res = _r
                r_idx = _r_idx

                break

        print(origin_q, q, res, r_idx)

        if q_i !=0:
            r_idx+=1

        for idx, r in enumerate(sorted_R[r_idx:]):
            if q < r:
                break
            else:
                res += 1
                q-=r

                memo.insert(0, (memo[0][0]+r, idx+r_idx))

        print('memo',memo)
        print(res)

def after():

    N,Q = map(int, input().split())
    R = list(map(int, input().split()))

    sorted_R = sorted(R)

    memo = [0]*N
    memo[0] = sorted_R[0]
    for i, r in enumerate(sorted_R[1:]):

        memo[i+1] = memo[i] + r

    # print(sorted_R)
    # print(memo)

    def find_le_idx(a, x):
        # 'Find rightmost value less than or equal to x'

        i = bisect.bisect_right(a, x)
        if i:
            return i-1
        # raise ValueError
        return -1

    for i in range(Q):
        q = int(input())

        res = find_le_idx(memo, q)
        # print(q,res+1)
        print(res+1)




if __name__ == '__main__':

    # main()
    after()

    # bisect便利