
def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))

    sumA = sum(A)
    sumL = L*N
    sumR = R*N

    x= 0
    y= N

    if sumA < sumL and sumA <sumR:
        print(sumA)
        return

    res = sumA
    for y in range(N-1, 0, -1):
        for x in range(1, y):
            r = L*x+R*(N-y)
            if x<y-1:
                r+=sum(A[x:y])
            res = min(res, r)

    print(res)

def main2():

    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))

    accumlation = 0

    result = R*N

    for i in range(0, N):
        accumlation += min(accumlation+A[i], L*(i+1))
        result = min(result, accumlation+R*(N-1-i))
        
    print(result)


if __name__ == '__main__':
    main2()