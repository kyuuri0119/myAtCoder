def main():
    N = int(input())

    num = str(bin(N))
    # print(num)
    c = 0
    for i in range(len(num)):
        if num[-(i+1)] == '0':
            c+=1
        else:
            break

    print(c)



if __name__ == '__main__':
    main()