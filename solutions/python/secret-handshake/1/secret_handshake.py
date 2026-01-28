def commands(binary_str):
    actions = ['jump',
               'close your eyes',
               'double blink',
               'wink']
    Secret_Handshake = []
    for index, item in enumerate(binary_str[1:]):
        if int(item) == 1:
            Secret_Handshake.append(actions[index])

    return Secret_Handshake[::-1] if binary_str[0] == '0' else Secret_Handshake
