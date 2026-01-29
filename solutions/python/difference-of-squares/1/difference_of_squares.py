def square_of_sum(number):
    return ((1 + number) * number // 2) ** 2


def sum_of_squares(number):
    sum = 0
    for one in range(1,number + 1):
        sum += one ** 2
    return sum

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
