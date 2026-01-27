def is_armstrong_number(number):
    number_str = str(number)
    length = len(number_str)
    sum_str = 0
    for index in number_str:
        sum_str += int(index) ** length

    return sum_str == number