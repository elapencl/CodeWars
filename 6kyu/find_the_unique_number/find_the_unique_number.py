def find_uniq(arr):
    list = []
    count1 = 0
    count2 = 0
    for i in arr:
        if i not in list:
            list.append(i)
    for i in arr:
        if i == list[0]:
            count1 += 1
        elif i == list[1]:
            count2 += 1
    if count2 > count1:
        n = list[0]
    else:
        n = list[1]
    return n   
