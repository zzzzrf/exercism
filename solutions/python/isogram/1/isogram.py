def is_isogram(string):
    string=string.lower()
    hyphens = string.count('-')
    spaces = string.count(' ')
    hyphens_fix = hyphens - 1 if hyphens > 1 else 0
    spaces_fix = spaces - 1 if spaces > 1 else 0

    return len(string) == (len(set(string)) + hyphens_fix + spaces_fix)
