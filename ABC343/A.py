
def main():
    A, B= map(int,input().split())

    for i in range(10):
        if i != A+B:
            print(i)
            return


if __name__ == '__main__':
    main()