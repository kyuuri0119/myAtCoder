import itertools


def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    b = map(str, sorted(a_list, reverse=True)[:3])

    anagram_list = [int(''.join(v)) for v in itertools.permutations(b)]


    print(max(anagram_list))

if __name__ == '__main__':
    main()