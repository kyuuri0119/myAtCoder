def main():
    S = input()

    res = {S[i:j] for i in range(len(S)) for j in range(i+1, len(S)+1)}

    print(len(res))




if __name__ == '__main__':
    main()