import itertools


def main():
    N = int(input())
    bit = list(bin(N))[2:]

    result_index = []

    # print(int('0b' + ''.join(bit), 0))
    # print('0b' + ''.join(bit))

    reversed_bit = list(reversed(bit))

    index_of_1 = [idx for idx, _ in enumerate(bit) if reversed_bit[idx] == '1']
    # print(index_of_1)

    for length in range(1, len(index_of_1)):
        result_index.extend(itertools.combinations(index_of_1, length))
    # print(result_index)

    result = [0, N]
    for pat in result_index:
        bits = [0]*60
        for i in pat:
            bits[i] = 1

        # print(bits, '0b'+''.join(map(str, reversed(bits))))
        result.append(int('0b'+''.join(map(str, reversed(bits))), 0))

    for r in sorted(set(result)):
        print(r)


if __name__ == '__main__':
    main()
