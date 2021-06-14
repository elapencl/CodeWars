def filter_list(l):
    filter =[]
    for i in l:
        if type(i) == int:
            filter.append(i)
    return filter
