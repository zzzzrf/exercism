def score(x, y):
    distence = x**2 + y**2
    if distence > 100:
        return 0
    if distence > 25:
        return 1
    if distence > 1:
        return 5

    return 10
