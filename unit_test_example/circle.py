from math import pi

def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError('Неверные данные')
    if r < 0:
        raise ValueError('Радиус не может быть отрицательным')
    return pi*r**2
