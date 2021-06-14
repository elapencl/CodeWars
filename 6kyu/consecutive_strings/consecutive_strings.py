def longest_consec(strarr, k):
    list = []
    result = ""
    count = p = 0
    k_original = k
    if k > int(len(strarr)) or k < 0 or k == 0 or strarr == []:
        return ""
    elif k == 1:
        return max(strarr, key=len)
    else:
        while count < int(len(strarr)):
            result = ''.join(strarr[i] for i in range(p, k))
            list.append(result)
            p += 1
            count += 1
            if k > int(len(strarr)) or k == int(len(strarr)):
                break
            k += 1
        return max(list, key=len)
