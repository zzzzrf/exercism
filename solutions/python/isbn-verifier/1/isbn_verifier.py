def is_valid(isbn):
    isbn = list(isbn.replace('-',''))
    if len(isbn) != 10:
        return False

    for index,item in enumerate(isbn):
        if str(item).isalpha():
            if index < 9:
                return False
            elif item != 'X':
                return False
            else:
                isbn[index] = '10'

    sum = 0
    for index in range(10):
        sum += int(isbn[index]) * (10 - index)
    return sum % 11 == 0
