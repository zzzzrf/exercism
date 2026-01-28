RESISTOR_COLOR = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9,
}

def label(colors):
    tmp = RESISTOR_COLOR[colors[0]] * 10 + RESISTOR_COLOR[colors[1]]
    for color in colors[2:3]:
        tmp *= 10 ** RESISTOR_COLOR[color]
    
    if tmp < 1000:
        return str(tmp) + ' ohms'
    if tmp < 1000000:
        return str(int (tmp/1000)) + ' kiloohms'
    if tmp < 1000000000:
        return str(int (tmp/1000000)) + ' megaohms'
    if tmp < 1000000000000:
        return str(int (tmp/1000000000)) + ' gigaohms'
