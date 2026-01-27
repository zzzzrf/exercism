def response(hey_bob):
    hey_bob = hey_bob.strip(' \t\r\n')
    if len(hey_bob) == 0:
        return 'Fine. Be that way!'
    if hey_bob.isupper():
        if hey_bob[-1] == '?':
            return 'Calm down, I know what I\'m doing!'
        else:
            return 'Whoa, chill out!'
    if hey_bob[-1] == '?':
        return 'Sure.'
    
    return 'Whatever.'
