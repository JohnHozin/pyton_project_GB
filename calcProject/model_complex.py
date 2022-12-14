x = 0
y = 0


def init(a, b, c, d):
    global x, y
    x = complex(a, b)
    y = complex(c, d)


def return_x():
    return x


def return_y():
    return y


def do_sum():
    return round_complex(x + y)


def do_sub():
    return round_complex(x - y)


def do_mult():
    return round_complex(x * y)


def do_div():
    return round_complex(x / y)


def round_complex(z):
    return complex(round(z.real, 3), round(z.imag, 3))
