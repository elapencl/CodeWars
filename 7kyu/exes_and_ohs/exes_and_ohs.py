def xo(s):
    j = k = i = 0
    while i < len(s):
        if s[i].lower() == 'x':
            j += 1
        elif s[i].lower() == 'o':
            k += 1
        i += 1
    if j != k:
        return False
    elif j == k:
        return True
