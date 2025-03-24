from math import pi, sqrt

choice = int(input("Выбор фигуры: \n1 - треугольник \n2 - прямоугольник \n3 - круг \n: "))
if choice == 1:
    a = int(input("Введите сторону а: "))
    b = int(input("Введите сторону b: "))
    c = int(input("Введите сторону c: "))
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print("Площадь треугольника:", round(s, 2))
elif choice == 2:
    a = int(input("Введите сторону а: "))
    b = int(input("Введите сторону b: "))
    print("Площадь прямоугольника:", a * b)
elif choice == 3:
    radius = int(input("Введите радиус окружности: "))
    print("Площадь окружности:", round(pi * (radius ** 2), 2))
