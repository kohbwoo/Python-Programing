def Q520(src):
    if src == "":
        return ""
    if len(src) == 1:
        return src

    tmp = 1
    ans = ""
    for i in range(1, len(src)):
        if src[i - 1] == src[i]:
            tmp += 1
        else:
            ans += (src[i - 1] + str(tmp))
            tmp = 1
        if i == len(src) - 1:
            ans += (src[i] + str(tmp))

    return ans


print(Q520('a'))
print(Q520('ab'))
print(Q520('aaaabbb'))
print(Q520('aaaabccccaaaaacccfg'))
