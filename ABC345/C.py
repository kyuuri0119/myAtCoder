import string


def main():
    S = input()

    res = 0

    ketu = {a: 0 for a in string.ascii_lowercase}
    max_ketu = 0

    ketu[S[-1]] +=1
    max_ketu += 1

    for i in reversed(range(len(S)-1)):
        res += max_ketu - ketu[S[i]]
        ketu[S[i]] += 1
        max_ketu  += 1
        # print(S[i], ketu)

    for k,v in ketu.items():
        if v>1:
            res+=1
            break

    print(res)

    # res_ =set()
    # for i in range(len(S)-1):
    #     for j in range(i+1, len(S)):
    #         s = S[:i] + S[j] + S[i+1:j] + S[i] + S[j+1:]
    #         res_.add(s)
    #
    # print(res_)
    #
    # print(len(res_))

if __name__ == '__main__':
    main()

