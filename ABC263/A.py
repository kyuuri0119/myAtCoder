def main():
    s = input().split()

    if len(set(s)) == 2 and s.count(s[0]) in [2, 3]:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()