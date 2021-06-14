def descending_order(num):
    num = list(map(int,str(num)))
    num = sorted(num, reverse=True)
    newnum = [str(i) for i in num]
    num = int("".join(newnum))
    return num
