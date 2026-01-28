def rotate(text, key):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    list1 = list(alpha)
    list2 = list(alpha.upper())
    list3 = list1[key:] + list1[0:key]
    list4 = list2[key:] + list2[0:key]

    cipher = ''
    for latter in text:
        if latter.isupper():
            index = list2.index(latter)
            cipher += list4[index]
        elif latter.islower():
            index = list1.index(latter)
            cipher += list3[index]
        else:
            cipher += latter
    return cipher
