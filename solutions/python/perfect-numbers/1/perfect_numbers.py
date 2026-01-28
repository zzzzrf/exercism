def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    sum = 0
    for item in range(1,number):
        if not(number % item) :
            sum += item
    if number == sum:
        return 'perfect'
    if number > sum:
        return 'deficient'
    return 'abundant'
