def solution(number):
    count = 0
    sum = 0
    while count < number:
        if count%3 == 0 or count%5 == 0:
            sum = sum + count
        count += 1
    return(sum)
