def find_short(s):
    list = s.split(' ', len(s))
    count = []
    j = 0
    for i in list:
        count.append(len(i))
    l = min(count)
    return l 
