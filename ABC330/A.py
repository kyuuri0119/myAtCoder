
def main():
    N, L = map(int,input().split())
    A = list(map(int,input().split()))

    ans = [a for a in A if a >= L]
    print(len(ans))

if __name__ == '__main__':
    main()