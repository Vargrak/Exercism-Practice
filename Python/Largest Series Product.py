def largest_product(series, size):
    if size == 0:
        return 1
    if len(series) < size:
        raise ValueError("span must be smaller than string length")
    if size < 0:
        raise ValueError("span must be greater than zero")
    if series.isdigit() == False:
        raise ValueError("digits input must only contain digits")

    list_of_series = [series[x:x+size] for x in range(0, len(series)) if len(series[x:x+size]) == size]

    largest_product_ = 0
    for chunk in list_of_series:
        sum_ = 1
        for char in chunk:
            sum_ = sum_ * int(char)
        if sum_ > largest_product_:
            largest_product_ = sum_
    return largest_product_