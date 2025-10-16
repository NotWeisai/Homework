def max(a, b, c = None):
    if c is None:       # Если есть только два числа
        if a >= b:
            return a
        else:
            return b
    else:           # Если есть три числа
        if a >= b and a >= c:
            return a
        elif b >= a and b >= c:
            return b
        else:
            return c

print(max())