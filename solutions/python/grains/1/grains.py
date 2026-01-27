SQUARES_COUNT = 64

def square(number):
    if number < 1 or number > SQUARES_COUNT:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    index = 1
    ans = 0
    while index <= SQUARES_COUNT:
        ans += square(index)
    return ans
