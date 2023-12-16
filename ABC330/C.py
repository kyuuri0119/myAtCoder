import math


def main():
    D = int(input())

    sq_d = math.sqrt(D)
    f_sq_d = math.floor(sq_d)
    # print(sq_d, f_sq_d)
    old = 2*math.pow(10, 12)
    # print(old, math.sqrt(old))
    ans =old
    for x in reversed(range(0, f_sq_d+2)):
        xx =math.pow(x,2)
        for y in range(0, f_sq_d+2):
            res = abs(xx + math.pow(y,2) -D)
            if res > ans:

                break
            else:
                ans = res

            # print(ans, x, y)
    print(int(ans))

def after():
    D = int(input())

    sq_d = math.sqrt(D)
    f_sq_d = math.floor(sq_d)
    # print(sq_d, f_sq_d)

    ans = 2* math.pow(10, 12)

    d = {ans: (0,0)}

    for x in range(0, f_sq_d+2):
        c = math.pow(x,2) - D
        if c >= 0:
            y = 0
            if ans > abs(math.pow(y,2)+c):
                ans = min(ans, abs(math.pow(y, 2) + c))
                d[ans] = (x, y)
        else:
            y = math.floor(math.sqrt(abs(c)))
            if ans > abs(math.pow(y,2)+c):
                ans = min(ans, abs(math.pow(y, 2) + c))
                d[ans] = (x, y)

            y = math.floor(math.sqrt(abs(c)))+1
            if ans > abs(math.pow(y,2)+c):
                ans = min(ans, abs(math.pow(y, 2) + c))
                d[ans] = (x, y)

    # print(int(ans), d[ans])
    print(int(ans))




if __name__ == '__main__':
    after()