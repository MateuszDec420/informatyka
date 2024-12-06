def f(x):
    return x * x + 1


def calka(a, b):
    E = 1000
    c = 0
    w = (b-a)/E
    for i in range(E):
        h = f(a + i * w)
        c += w*h
    return c


print(calka(0, 2))