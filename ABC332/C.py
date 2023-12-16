def main():
    N, M = map(int, input().split())
    S = input()

    b_log_t = 0
    u_log_t = 0
    u_t = 0

    for s in S:
        if s == '0':
            u_t = 0
            u_log_t = 0
        elif s == '1':
            if u_t < M:
                u_t += 1
            else:
                if u_log_t < b_log_t:
                    u_log_t+=1
                else:
                    u_log_t+=1
                    b_log_t+=1
        else:
            if u_log_t < b_log_t:
                u_log_t += 1
            else:
                u_log_t += 1
                b_log_t += 1

    print(b_log_t)

if __name__ == '__main__':
    main()