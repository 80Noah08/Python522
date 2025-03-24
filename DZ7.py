from math import pi, sqrt


def area(figure):
    if figure == 1:
        a = int(input("Ведите значение a: "))
        b = int(input("Ведите значение b: "))
        c = int(input("Ведите значение c: "))
        p = (a + b + c) / 2
        res = sqrt(p * (p - a) * (p - b) * (p - c))
        return round(res, 2)
    elif figure == 2:
        a = int(input("Ведите значение a: "))
        b = int(input("Ведите значение b: "))
        res = a * b
        return res
    elif figure == 3:
        a = int(input("Ведите радиус: "))
        res = round(pi * (a ** 2), 2)
        return res


x = int(input("Выберите фигуру для нахождения площади:\n1-Треугольник\n2-Прямоугольник\n3-Круг\n: "))
print(area(x))






