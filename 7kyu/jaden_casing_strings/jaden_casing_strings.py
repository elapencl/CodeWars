def to_jaden_case(string):
    list = string.split()
    newlist = []
    for i in list:
        newlist.append(i.capitalize())
    list = ' '.join(newlist)
    return list
