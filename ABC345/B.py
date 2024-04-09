def main():
    X = int(input())

    def ceil(N, div):
        return (N+div-1)//div

    print(ceil(X, 10))



if __name__ == '__main__':
    main()