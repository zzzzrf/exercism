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

RESISTOR_TOLERANCE = {
    'grey': '0.05%',
    'violet': '0.1%',
    'blue': '0.25%',
    'green': '0.5%',
    'brown': '1%',
    'red': '2%',
    'gold': '5%',
    'silver': '10%',
}

def resistor_label(colors):
    if RESISTOR_COLOR[colors[0]] == 0:
        return '0 ohms'

    tmp = 0
    for index, color in enumerate(colors[0:-2]):
        tmp *= 10
        tmp += RESISTOR_COLOR[color]

    tmp *= 10 ** RESISTOR_COLOR[colors[-2]]

    def format_value(val):
        if val == int(val):
            return str(int(val))
        else:
            return str(val)

    if tmp < 1000:
        return format_value(tmp) + ' ohms ±' + RESISTOR_TOLERANCE[colors[-1]]
    if tmp < 1000000:
        return format_value( (tmp/1000)) + ' kiloohms ±' + RESISTOR_TOLERANCE[colors[-1]]
    if tmp < 1000000000:
        return format_value( (tmp/1000000)) + ' megaohms ±' + RESISTOR_TOLERANCE[colors[-1]]
    if tmp < 1000000000000:
        return format_value( (tmp/1000000000)) + ' gigaohms ±' + RESISTOR_TOLERANCE[colors[-1]]

print(resistor_label(["red", "black", "red", "green"]))