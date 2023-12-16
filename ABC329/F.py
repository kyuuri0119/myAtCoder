
def main():
    N, Q = map(int, input().split())
    C = list(map(int, input().split()))

    box:dict[int, list[int]] = {i: [c] for i,c in enumerate(C)}

    for i in range(Q):
        a, b = map(int, input().split())
        r = set([*box[a-1], *box[b-1]])
        box[b-1]= list(r)
        box[a-1] = []
        print(len(box[b-1]))


def after():
    N, Q = map(int, input().split())
    C = list(map(int, input().split()))

    box:dict[int, set[int]] = {i: {c} for i,c in enumerate(C)}

    for i in range(Q):
        a, b = map(int, input().split())

        if len(box[b-1]) >= len(box[a-1]):
            for c in box[a-1]:
                box[b-1].add(c)
            box[a-1].clear()
        else:
            for c in box[b-1]:
                box[a-1].add(c)
            box[a-1], box[b-1] = box[b-1], box[a-1]
            box[a-1].clear()

        print(len(box[b-1]))




if __name__ == '__main__':
    after()