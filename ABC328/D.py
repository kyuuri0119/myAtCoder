def main():

    S = str(input())

    has_rem = S.find('ABC')
    if has_rem>=0:
        while has_rem>=0:
            left_remain = S[:has_rem]
            S = left_remain+S[has_rem+3:]
            # print(S)
            has_rem = S.find('ABC')
            # print(has_rem)

    print(S)

def after():
    S =str(input())

    stack = []
    for s in S:
        stack.append(s)
        if len(stack) >= 3:
            if "".join(stack[-3:]) == 'ABC':
                del stack[-3:]
    print("".join(stack))

if __name__ == '__main__':
    # main()
    after()