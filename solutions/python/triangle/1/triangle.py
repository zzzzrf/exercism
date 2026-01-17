def is_triangle(sides):
    if 0 in sides:
        return False
    a, b, c = sides
    return (a + b >=c and b + c >= a and a + c >= b)

def equilateral(sides):
    if is_triangle(sides) == False:
        return False
    a, b, c = sides
    return (a == b == c)

def isosceles(sides):
    if is_triangle(sides) == False:
        return False
    a, b, c = sides
    return (a == b or a == c or b == c)

def scalene(sides):
    if is_triangle(sides) == False:
        return False
    a, b, c = sides
    return (a != b  and a != c and b != c)