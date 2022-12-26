x = 0
y = 0
z = 0


def init(a, b, c):
    global x
    global y
    global z
    x = a
    y = b
    z = c


def complete():
    if z == '+':
        return float(x) + float(y)
    elif z == '-':
        return float(x) - float(y)
    elif z == '*':
        return float(x) * float(y)
    elif z == '/':
        if float(y) == 0:
            return 'На ноль делить нельзя'
        else:
            return float(x) / float(y)
    else:
        print('Введите в формате a+b')
