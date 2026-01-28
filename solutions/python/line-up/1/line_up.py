def line_up(name, number):
    fix_str = 'th'
    if not ((number - 1) % 10):
        if ((number - 11) % 100):
            fix_str = 'st'
    if not ((number - 2) % 10):
        if ((number - 12) % 100):
            fix_str = 'nd'
    if not ((number - 3) % 10):
        if ((number - 13) % 100):
            fix_str = 'rd'
    return f"{name}, you are the {number}{fix_str} customer we serve today. Thank you!"

print(line_up("Mary", 1))