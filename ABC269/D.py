def main():
    N = int(input())

    coordinates = [tuple(map(int, input().split())) for i in range(N)]
    coordinates_str = {str(x) + ',' + str(y) for x, y in coordinates}

    for c in coordinates:
        if str(c[0]) + ',' + str(c[1]) not in coordinates_str:
            continue

        remove_connects(source=c, target=c, coordinates_str=coordinates_str)

    print(len(coordinates_str))


def remove_connects(source, target, coordinates_str):
    s = str(source[0]) + ',' + str(source[1])
    c = target
    connected = []
    for conn in get_connects_str(c):
        if s == conn:
            continue

        if conn in coordinates_str:
            connected.append(tuple(map(int, conn.split(','))))
        coordinates_str.discard(conn)

        # print('connected', connected)
        # print('result', coordinates_str)

    for c in connected:
        remove_connects(source=source, target=c, coordinates_str=coordinates_str)


def get_connects_str(target):
    return [str(x) + ',' + str(y)
            for x in [target[0] - 1, target[0], target[0] + 1]
            for y in [target[1] - 1, target[1], target[1] + 1]
            if not ((x == target[0] and y == target[1]) or (x == target[0] + 1 and y == target[1] - 1) or (
                    x == target[0] - 1 and y == target[1] + 1))
            if abs(x) <= 1000 and abs(y) <= 1000]


if __name__ == '__main__':
    main()
