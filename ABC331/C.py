from collections import defaultdict

def key_sort(dicts, reverse=False):
    dicts = sorted(dicts.items(), reverse=reverse)
    dicts = fruits = dict((x, y) for x, y in dicts)
    return dicts

def main():
    N = map(int, input().split())
    A = list(map(int, input().split()))

    memo = defaultdict(int)
    sum_memo = 0

    for a in A:
        memo[a] += a
        sum_memo += a

    sorted_memo = key_sort(memo)

    su = defaultdict(int)
    for i, k in enumerate(sorted_memo.keys()):
        sum_memo = sum_memo - sorted_memo[k]
        su[k] = sum_memo

    res = [su[a] for a in A]
    # print(' '.join(res))
    print(*res)


if __name__ == '__main__':
    main()