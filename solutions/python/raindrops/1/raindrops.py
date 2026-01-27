def convert(number):
    return_str = ''
    if number % 3 == 0:
        return_str += 'Pling'
    if number % 5 == 0:
        return_str += 'Plang'
    if number % 7 == 0:
        return_str += 'Plong'
    if return_str == '':
        return_str += str(number)
    return return_str
