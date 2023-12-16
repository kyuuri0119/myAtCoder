def main():
    s = input()
    t = input()

    p = ['A', 'B', 'C', 'D', 'E']

    pat1 = [p[i%5]+p[(i+1)%5] for i in range(5)]
    pat1.extend([p[(i+1)%5]+p[(i)%5] for i in range(5)])
    pat2 =  [p[i%5]+p[(i+2)%5] for i in range(5)]
    pat2.extend( [p[(i+2)%5]+ p[(i)%5] for i in range(5)])

    if s in pat1 and t in pat1:
        print('Yes')

    elif s in pat2 and t in pat2:
        print('Yes')

    else:
        print('No')

if __name__ == '__main__':
    main()