def series_sum(n):
    count = 0
    numerator = denominator = series = 1
    if n == 1:
        return "{:.2f}".format(numerator)
    elif n == 0.00:
        return "{:.2f}".format(count)
    else:
        while count<(n-1):
            denominator = denominator + 3
            number = numerator/denominator
            series = series + number
            count += 1
        result = "{:.2f}".format(series)
        return result
