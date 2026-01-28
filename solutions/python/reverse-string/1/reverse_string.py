def reverse(text):
    index = len(text)
    reversed = ''
    while index > 0:
        reversed += text[index-1]
        index -= 1
    return reversed
