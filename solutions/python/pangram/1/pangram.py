PANGRAM_SETS = {'A','B','C','D','E','F','G',
                'H','I','J','K','L','M','N',
                'O','P','Q','R','S','T',
                'U','V','W','X','Y','Z'}

def is_pangram(sentence):
    sentence = str(sentence).upper()
    return PANGRAM_SETS <= set(sentence)
