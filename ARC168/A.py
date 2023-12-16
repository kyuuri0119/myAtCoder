
class BIT:

    # 初期化
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n+1)

    # 加算
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i  # LSBの計算
        print(self.tree)

    # インデックス0からiまでの総和を計算
    def sum(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i  # LSBの計算
            print(i, total)

        return total

def main():
    N=int(input())
    S=str(input())

    ans = 0

    S+='_'
    arr = [N]*(N+1)
    for i, s in enumerate(S[:N]):

        if s == '<':
            arr[i+1] = arr[i]+1
        elif s == '>':
            arr[i+1] = arr[i]-1

    # print(arr)

    # max_arr = max(arr)
    min_arr = min(arr)
    bit = BIT(N+1)
    for i in range(len(arr)-1):
        ans += i - bit.sum(arr[i]-min_arr+1)
        print(i, arr, ans)
        bit.add(arr[i]-min_arr+1, 1)

    print(ans)

# def after():
#     N=int(input())
#     S=str(input())
#
#     ans =0
#     cnt = 0
#     for s in S:
#         if s == ">":
#

if __name__ == '__main__':
    main()