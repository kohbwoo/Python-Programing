def Q520(src):
    print("src = '" + src + "'")
    ans = ""

    if src == "":  # src가 공백인경우
        return "output = '" + src + "'\n"
    elif len(src) == 1:  # src가 인자가 한개인경우
        return "output = '" + src + "1'\n"
    tmp = 1
    # [0][1][2][3][4][5]
    for i in range(1, len(src)):
        if src[i - 1] == src[i]:
            tmp += 1
        else:
            ans += (src[i - 1] + str(tmp))
            tmp = 1
        if i == len(src) - 1:
            ans += (src[i] + str(tmp))
    return "output = '" + ans + "'\n"

print(Q520(""))
print(Q520('a'))
print(Q520('ab'))
print(Q520('aaaabbb'))
print(Q520('aaaabccccaaaaacccfg'))
