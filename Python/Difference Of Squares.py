def square_of_sum(number):
    return sum([x for x in range(0, number)])**2

def sum_of_squares(number):
    return sum([x**2 for x in range(0, number)])

def difference_of_squares(number):
    return max(sum_of_squares(number) - square_of_sum(number), square_of_sum(number) - sum_of_squares(number))


print(difference_of_squares(1))