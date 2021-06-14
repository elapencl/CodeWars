def divisors(integer):
    list = []
    count = 2
    while count < integer:
        if integer%count == 0:
            list.append(count)
        count = count + 1
    if len(list) == 0:
        return str(integer) + " is prime"
    else:
        return list
