# name = "admin"
# print("Hello", name)
# age = 20
# print(age)
#
# print(type(name))
# print(type(age))
#
#
# print(id(name))
# print(id(age))
# from sys import base_prefix
# import os
# import re
# from sys import set_int_max_str_digits
# from sys import prefix
# import json
# import string
#
# from car.electro_car import ElectroCar

# a = b = c = 1
# a, b, c = 5, "Hello", 7.2
# print(a)
# print(b)
# print(c)

# name = "admin"
# print(name)

# import keyword
# print(keyword.kwlist)

# PI = 3.14
# print(PI)
#
# PI = 2
# print(PI)


# a = 5
# print(a)
# a = "Hello"
# print(a)

# a = 5
# b = 20
# print("a:", a)
# print("b:", b)
#
# c = a  # 1
# a = b  # 2
# b = c  # 1


# s1 = 'Hello'
# s2 = 'Python'
# s3 = s1 + s2 # конкатенация
# print (s3)


# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(7 / 2)   # вещественное деление
# print(7 // 2)   # целочисленное деление
# print(7 ** 2)   # возведение в степень
# print(7 % 2)   # остаток от деления


# a = 5
# b = 7
# c = 3
# d = 5 + 7 + 3
# print(d)
# f = 5 * 7 * 3
# print(f)
# x = d / 3
# print(x)


# num = 4321
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)

# num1 = '2'
# num2 = 3
# res = num1 + str(num2)
# print(res)

# print(int(3.981))
# print(type(round(3.981)))      #round - округлуение
# print(type(round(3.589, 2)))

# num1 = "2.5"
# num2 = 10
# res = float(num1) + num2  # 2.5 + 10
# print(res)

# name = "Виктор"
# age = 20
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут" + name + ". Мне" + str(age) + "лет.")
# print("Меня зовут ", name, ". Мне ", age, " лет. ", sep="", end="")
# print("Hello Python")

# name = input("Введите имя: ")
# print("Hello,", name)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# # num = int(num)
# # power = int(power)
# res = num ** power
# print("Число", num, "в степени", "равно: ", res)

# num1 = float(input("Введите число: "))
# num2 = float(input("Введите число: "))
# num3 = float(input("Введите число: "))
# num4 = float(input("Введите число: "))
# a = num1 + num2
# b = num3 + num4
# c = a / b
# print(round(c, 2))

# b1 = True   #1
# b2 = False   #2
#
# print(int(b1))
# print(int(b2))
# print(b1 +5)
# print(b2 +5)

# print(bool("Python"))
# print(bool(""))
# print(bool(" "))
# print(bool(-5))
# print(bool(0))
# print(bool(0.2))
# print(bool(0.0))
# print(bool(True))
# print(bool(False))
# print(bool(None))

# print(5 == 5)
# print(5 == 3)
# print(2 + 5 == 3 + 4)
# print(2 + 5 != 3 + 4)
# print(8 > 5)
# print(8 >= 8)
# print(5 <= 5)
# print("hello" > "Hello")   # сравнивает по коду символов 104>72

# print(2 < 4 < 9)  # True : True => True
# print(2 > 4 < 9)  # False : True => False
#
# print(2 * 5 > 7 >= 4 + 3)    # True : True => True
# print(3 * 3 <= 7 >= 2)    # False : True => False

# print(5 - 3 == 2 and 1 + 3 == 4)   # True and True => True
# print(5 - 3 > 2 and 1 + 3 == 4)   # False and True => False
# print(5 - 3 == 2 and 1 + 3 < 4)   # True and False => False
# print(5 - 3 > 2 and 1 + 3 < 4)   # False and False => False

# print(5 - 3 == 2 or 1 + 3 == 4)   # True and True => True
# print(5 - 3 == 2 or 1 + 3 < 4)   # True and False => True
# print(5 - 3 > 2 or 1 + 3 == 4)   # False and True => True
# print(5 - 3 > 2 or 1 + 3 < 4)   # False and False => False

# print(not 9 - 5) # not True => False
# print(not 7 - 7) # not False => True

# a = 10
# b = 10
# if a > b:
#     print(a," > ", b)
# if b > a:
#     print(b, " >", a)
# if b == a:
#     print(b, "==", a)

# cnt = 11
# if cnt < 10:
#     cnt = cnt + 1
# else:
#     cnt = cnt - 1
# print(cnt)

# a = 40
# b = 20
# if a > b:
#     print(a, " > ", b)
# elif a == b:
#     print(b, "==", a)
# else:
#     print(b, " > ", a)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
#     print("Приятного просмотра")
# else:
#     print("Доступ запрещен")


# a = input("Введите значение первой стороны: "10)
# b = input("Введите значение второй стороны: ")
# c = input("Введите значение третьей стороны: ")
#
# if a == b == c:
#     print(" Треугольник равносторонний")
# elif a == b or a == c or b == c:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:    # (day >= 1) and (day <= 5)
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
# elif day == 6 or day == 7:
#         print("Выходной день - ", end="")
#         if day == 6:
#             print("Суббота")
#         if day == 7:
#             print("Воскресенье")
# else:
#     print("Такого дня недели не существует")

# day = int(input("Введите месяц (цифрой): "))
# if day <= 2 or day == 12:
#     print("Зима")
# elif day <= 3 or day <= 5:
#     print("Весна")
# elif day <= 6 or day <= 8:
#     print("Лето")
# elif day <= 9 or day <= 11:
#     print("Осень")
# else:
#     print("Такого времени года не существует")

# n = int(input("Введите кол-во ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")

# match выражение:
#     case шаблон_1:
#         действие_1
#     # case шаблон_2:
#         действие_2

# password = "qwerty"

# match password:
#     case "admin":
#         print("Администратор")
#     case "user":
#         print("Пользователь")
#     case _:
#         print("Пароль не верен")

# day = "понедельник"
# time = 13
# match day:
#     case "понедельник" | "вторник" | "среда" | "четверг" | "пятница" if 9 <= time <= 12 or 14 <= time <= 17:
#         print("рабочий день")
#     case "суббота" | "воскресенье":
#         print("выходной день")
#     case _:
#         print("такого дня недели не существует или не рабочее время")

# a, b = 30, 20
#
# print(a if a < b else b)
#
# a, b = 30, 20
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# try:    # попытаться
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или Нельзя делить на ноль")
# else:     # когда в блоке try не возникло исключений
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally: # выполнится в любом случае
#     print("Конец программы")


# a = input("Введите первое число: ")   # 2
# b = input("Введите второе число: ")   # 5
#
# try:
#     a = int(a)
#     b = int(b)
# except ValueError:
#     a = str(a)
# finally:
#     print(a + b)

# Циклы

# # while условие:
# #     блок_инструкций
# i = 0  # счетчик
# while i < 5:  #  условие
#     print("i =", i)
#     i += 1   # изменениие счетчика

# итерация - один шаг цикла

# i = 1
# while i < 100:
#     print("i =", i)
#     i *= 10

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1


# i = 2
# while i <= 20:
#     print(i, end=" ")
#     i += 2

# i = 2
# while i <= 20:
#     if i % 2:
#         print(i, end=" ")
#     i += 1

# n = int(input("Количество символов: "))
# # print("*" * n)
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# n = int(input("Количество символов: "))
# i = 0
# while i < n:
#     if i % 2 == 0:
#         print("+", end="")
#     else:
#         print("-", end="")
#     i += 1

# n = int(input("Количество символов: "))
# while n > 0:
#     print("*", end="")
#     n -= 1

# a = int(input("Введите начало диапозона: "))
# b = int(input("Введите конец диапозона: "))
# res = 0
# while a <= b:
#     if a % 2:
#         print(a, end=" ")
#         res += a # res = res + a
#     a += 1
# print("\nСумма: ", res)

# n = input("Введите целое число: ")
#
# while type(n) is not int: #!= int
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое: ")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, ш =", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# for element in collection:
#  print(element)

# for i in "Hello!", "World":
#     print(i)

# range(start, stop, step)

# print(range(0, 8, 2))

# for i in range(0, 10, 1):  # i = 0, i < 10, i += 1   # i > 0, i -= 1
#     print(i, end=" ")
#
# print()
#
# i = 1
# while i <= 10:
#     print(i, end=" ")
#     i *= 2

# a = int(input("Введите целое число: "))
#
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")
# print()
#
# for i in range(11, 100, 11):
#     print(i, end=" ")

# for i in range(0, 3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("Цикл закончен")

# for i in range(3):  # 0
#     print("+++")
#     for j in range(2):   # 0
#         print("-----")

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# #
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
# #
#     print()

# letter = [i * 2 for i in "Hello"]
# print(letter)
#
# for i in "Hello":
#     print(i * 2)

# num = [i for i in range(30) if i % 2 == 0]
# print(num)
#
# for i in range(30):
#     if i % 2 == 0:
#         print(i, end=", ")


# Список (list)
# nums = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
# print(nums)
# print(type(nums))
# print(nums[0])
# print(nums[1])
# print(nums[10])
# print(nums[-1])
# print("Кол-во:", len(nums))
# nums[1] = 256
# nums[3] += 100
# print(nums)

# s = []
# print(s)
# print(type(s))
#
# t = list()
# print(t)
# print(type(t))
# print(range(0, 8, 2))
# print(list(range(1, 18, 2)))

# a = [1, 3, 5, 7, 9]
# b = [11, 13, 15, 17]
# print(a + b)
# print(a * 2)

# a = [1, 3, 5, 7, 9]
#
# for i in a:
#     print(i)

# a = [0 for i in range(5)]
# print(a)

# a = [i for i in range(5)]
# print(a)

# n = 15
# a = [i ** 2 for i in range(2, n)]
# print(a)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input(" -> "))
# print(a)
#
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# lst = [9, 6, 3, 5]

# for i in range(len(lst)):   # 0 1 2 3
#     print(lst[i], end=" ")
#
# print()
#
# for v in lst:  # 9 6 3 5
#     print(v, end=" ")

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# res = 0
# # for i in range(len(a)):
# #     if a[i] < 0:
# #         res += a[i]
#
# for i in a:
#     if i < 0:
#         res += i
# print(res)

# n = list(range(21, 41))
# print("Список: ", n)
# count = sum_ = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         count += 1
#     else:
#         sum_ += n[i]
# print("Кол-во четных элементов: ", count)
# print("Сумма нечетных элементов: ", sum_)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=" ")
# print()
# for i in range(0, len(a), 2):
#     print(a[i], end=" ")

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# a = [9, 7, 8, 4, 2]
# print(a)
# a[0], a[1] = a[1], a[0]
# print(a)

# Срез

# список[start:stop:step]
# a = [9, 7, 8, 4, 2, 1, 3]
# print(a)
# print(a[1:4])    # с первого по четвертый не включая 4
# print(a[5:])    # с пятого по последныий
# print(a[1:4:2]) #  с первого по четвертый каждый второй
# print(a[::-2])
# print(a[5:2:-1])
# print(a[10:20])

# lst = list(range(1, 8))
# print(lst)
# print(lst[::-1])
# print(lst[::2])
# print(lst[1::2])
# print(lst[:1])
# print(lst[-1:])
# print(lst[3:4])
# print(lst[4:])
# print(lst[4:1:-1])
# print(lst[2:5])

# a = [1, 2, 3, 4, 5, 6, 7]
# print(a)
# a[1:3] = [0, 0, 0, 0]
# print(a)
# a[1:2] = [20]
# print(a)
# # a[2] = [120, 45]
# # print(a)
# a[100:111] = [100]
# print(a)
# print(a[-1])
# print(len(a))

# методы списков
# print(dir(list))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# s = [9, 7, 8, 4, 2, 1, 3]
# print(s)
# s.append(99)   # добавляет элемент в конец списка
# print(s)
# s.extend([11, 12, 13])   # добавляет другой список элементов в конец списка
# print(s)
# s.insert(2, 100)   # добавляет элемент (второй параметр) по заданному индексу(первый параметр)
# print(s)

# s.insert(20, 5)
# print(s)

# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x)
#     s.insert(0, x)  # [7, 8, 9]
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []  # [2, 1, 4, 3]

# for i in a:    # 5
#     for j in b:  # 4
#         if i in c:
#             continue
#         if i == j:   # 5 == 4
#             c.append(i)
#             break
# print(c)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
#
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print(c)

# a = [1, 2, 3, 4, 2]
# b = [11, 22, 33]
# c = []

# if len(b) > len(a):
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)

# a = [1, 2, 3, 4, 2]
# b = [11, 22, 33]
# c = []
#
# if len(a) > len(b):
#     a, b = b, a
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])

# s = [9, 7, 8, 4, 2, 1, 3]
# print(s)
# item = 7
# if item in s:
#     s.remove(item)   # удаляет первое вхождение элемента по значению
# print(s)

# last = s.pop()   # в таком виде удаляет последний элемент из списка
# print(last)
# print(s)
#
# try:
#     second = s.pop(10)   # удаляет элемент по заданному индексу
# except IndexError:
#     second = "Такого индекса нет"
# print(second)
# print(s)
#
# s.clear()  # удаляет элементы из списка
# print(s)

# s = [9, 7, 8, 4, 2, 1, 3]
# print(s)
#
# s[5:] = []
# print(s)
#
# del s[:]
# print(s)

# s = [9, 7, 8, 4, 2, 8, 1, 3]
# print(s)
#
# num = s.count(8)   # количество вхождений заданного элемента
# print(num)

# ind = s.index(8, 3, 7)   # ищет первое вхождение заданного элемента, возвращает индекс на котором
# # нашел элемент, можно задать диапазон поиска
# print(ind)
#
# a = [1, 2, 3]
# b = a.copy()
# print("a =", a, id(a))
# print("b =", b, id(b))
# b.append(20)
# print("a =", a)
# print("b =", b)
# a.append(100)
# print("a =", a, id(a))
# print("b =", b, id(b))

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(a)
# a.reverse()
# print(a)
# #
# a.sort()
# print(a)

# s = ["Виталий", "Сергей", "Александр", "Анна"]
# s.sort(key=len, reverse=True)
# print(s)
# b = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# lst = sorted(b, reverse=True)
# print("lst:", lst)

# print(random.random())
# print(random.randint(5, 10,))
# print(random.randrange(5, 10, 2))
# print(round(random.uniform(10.5, 25.5), 2))

# city_list = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# print(random.choice(city_list))
# print(random.choice(s))
# print(random.choices(city_list, k=3))
# print(random.choices(s, k=3))
# random.shuffle(s)
# print(s)

# mas = [random.randint(50, 100) for i in range(5)]
# print(mas)
# print(len(mas))
# print(max(mas))
# print(min(mas))
# print(sum(mas))

# mas = [random.randint(0,100) for i in range(10)]
# print(mas)
# max_ = max(mas)
# print(max_)
# mas.remove(max(mas))
# mas.insert(0, max_)
# print(mas)
#
# import random

# mas = [random.randint(0,100) for i in range(10)]
# print(mas)
#
# min_ = min(mas)
# print("Min", min_)
#
# ind = mas.index(min_)
# print("Index min:", ind)
#
# del mas[:ind]
# print(mas)
#
# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8,],
#     [9, 10, 11, 12]
# ]
# print(m)
#
# # print(len(m))
# # print(m[1][2])
# # print(m[2][1])
#
# print("Вариант 1")
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print("Вариант 2")
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# m = ["Hello", "World", [44, [1, 2, 3], 55, ["Python"]]]
# print(m)
# print(m[1][2])
# print(m[2][1][1])
# print(m[2][3][0][3])

# import math
#
# print(math.sqrt(4))
# print(math.ceil(3.2))
# print(math.floor(3.8))

# import math as m
#
# print(m.sqrt(4))
# print(m.ceil(3.2))
# print(m.floor(3.8))

# from math import *
#
# print(sqrt(4))
# print(ceil(3.2))
# print(floor(3.8))

# from math import sqrt, ceil, floor
#
# print(sqrt(4))
# print(ceil(3.2))
# print(floor(3.8))

# print(dir(list))

# from math import pi
# #
# # # print(pi)
# radius = int(input("Введите радиус окружности: "))
# print("Длина окружности:", round(2 * radius * pi, 2))

# import time
# import locale

# print(time.time())
# print(time.ctime(739210060))
# res = time.localtime()
# print(res)
# print(time.strftime("Today is %B %d, %Y"))
# # print(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(539210060)))
# locale.setlocale(locale.LC_ALL, "")
# print(time.strftime("Сегодня: %B %d, %Y"))

# start = time.time()
# print("Запуск программы")
# time.sleep(5)
# res = time.time() - start
# print("Программа выполнилась за", res, "секунд")

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Урок 8!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Функции


# def hello(name, age):    #аргументы
#     print("Меня зовут:,", name, "Мой возраст:", age)
#
#
# hello("Irina", 28)   #параметры
# hello("Ivan", 25)


# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum("abc", "def")


# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")


# def get_sum(a, b):
#     print("Сумма:", end=" ")
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)


# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 5))
# print(maximum(5, 15))


# def v(a, b):
#     if a > b:
#         return b - a
#     else:
#         return b + a
#
#
# a = int(input("Ведите число a: "))
# b = int(input("Ведите число b: "))
# print(v(a, b))


# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# def change(lst):
#     end = lst.pop()
#     start = lst.pop(0)
#     lst.append(start)
#     lst.insert(0, end)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))


# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))


# def one_big(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# if one_big(a, b):
#     print("Первое число больше второго")
# else:
#     print("второе число больше первого")
# print(one_big(10, 5))
# print(one_big(5, 10))


# def check_password(password):
#     has_apper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_apper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_apper and has_lower:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2, c=5))


# def set_param(count=20, symbol="-"):
#     print(symbol * count)
#
#
# set_param(10, "+")
# set_param(5, "*")
# set_param(15, "#")
# set_param(7)
# set_param()


# def display_info(name, age):
#     print("Name:", name, "\nAge", age)
#
#
# display_info("Irina", 23)
#
#
# def display_info(name, age):
#     print("Hello,", name)
#
#
# display_info("Irina", 23)
# display_info(age=23, name="Irina")
# display_info("Igor", age=23, name="Irina")


# lt1 = "Hello"
# lt2 = "Hello"
# print(lt1, id(lt1))
# print(lt2, id(lt2))
# print(lt1 == lt2)
# print(lt1 is lt2)
#
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1, id(lst1))
# print(lst2, id(lst2))
# print(lst1 == lst2)
# print(lst1 is lst2)

# lst1 = [1, 2, 3]
# print(lst1, id(lst1))
# lst1.append(4)
# print(lst1, id(lst1))
# lst1.pop(1)
# print(lst1, id(lst1))

# lt1 = "Hello"
# print(lt1, id(lt1))
# lt1 = lt1[1: -1]
# print(lt1, id(lt1))
# lt1 = lt1 + "!"
# print(lt1, id(lt1))

# a = 5
# print(a, id(a))
# a = 7
# print(a, id(a))


# Кортеж (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
# lst[1] = 100
# print(lst[1])

# a = ()
# print(a, type(a))
# b = tuple()
# print(b, type(b))

# a = (1, 2, 3, 4, 5, 6)
# print(a, type(a))
#
# b = tuple("Hello")
# print(b, type(b))

# b = tuple("Hello")
# print(b)
#
# print(b[1:3])

# s1 = tuple(input("-> ") for i in range(5))
# print(s1)
#
# from random import randint
#
# s1 = tuple(randint(50, 100) for i in range(5))
# print(s1)

# t1 = tuple("hello")
# t2 = tuple("world")
# print(t1)
# print(t2)
# t3 = t1 + t2
# print(t3 * 2)
# print(t3)
# print(t3.count("l"))
# print(t3.index("l", 4, -2))
# v = "e"
# if v in t3:
#     print(t3.index(v))

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) == 1:
#             return tpl[tpl.index(el):]
#         else:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:second]
#     else:
#         return tuple()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# t = (10, "Python",  True, [1, 2, 3], ["hello", "world"])
# print(t, id(t))
# t[4][0] = "new"
# print(t, id(t))
# print(len(t))
# t[4].append("hi")
# print(t, id(t))

# Распаковка кортежа

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t    # Распаковка кортежа
# print(x, y, z)

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# # user = get_user()
# # print(user)
# # first_name, year, married = user
#
# first_name, year, married = get_user()
# print(first_name, year, married)

# lst = [1, 2, 3, 4, 5, 6]
# print(lst, type(lst))
# tpl = tuple(lst)
# print(tpl, type(tpl))
# lst2 = list(tpl)
# print(lst2, type(lst2))

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries, end="\n\n")
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана: ", country_name, ", население = ", country_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население = ",  city_population, sep="")

# tpl = tuple(input("Введите строку: "))
# print(tpl)
# lst = []
# for i in range(len(tpl)):
#     if tpl[i] not in lst:
#         lst.append(tpl[i])
#
# for i in range(len(lst)):
#     print("Кол-во", lst[i], "=", tpl.count(lst[i]))


# Множество (set)

# s = {"red", "yellow", "green", "yellow", "green"}
# print(s, type(s))
# print(len(s))

# a = set("hello")
# print(a, type(a))

# s = {x * x for x in range(10)}
# print(s)

# lst = [1, 2, 3, 5, 2, 1, 4, 6, 3, 9, 5, 7, 2, 1]
# lst = ["red", "yellow", "green", "yellow", "green"]
# print(lst)
# num = set(lst)
# print(num)
# lst2 = list(num)
# print(lst2)

# t = {'green', 'red', 'yellow'}
# print('red' in t)
# print('blue' in t)
# for i in t:
#     print(i)

# lst = ['ab_1', 'ac_1', 'bc_1', 'bc_2']
# print({i for i in lst if 'a' in i})
# print(['A' + i[1:] if i [0] == 'a' else 'B' + i[1:] for i in lst])
# print(tuple(['A' + i[1:] if i [0] == 'a' else 'B' + i[1:] for i in lst if i[1] == 'c']))

# print(dir(set))

# a = {"red", "yellow", "green"}
# print(a)
# a.add("blue")
# print(a)
# # a.remove("yellow")
# # a.remove("black")    #KeyError
# color = "black"
# # if color in a:
# #     a.remove(color)
# # a.discard(color)
# # a.pop()
# a.clear()
# print(a)

# print({i / 2 for i in range(1000, 1010)})


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b
# # print(c)
# # a |= b
# # a.update(b)
# # print(a)
# # c = a % b
# # print(c)
# # a %= b
# # print(a)
# # c = a - b
# # print(c)
# # a -= b
# # print(a)
# c = a ^ b
# print(c)
# a ^= b
# print(a)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# c = a <= b
# print(c)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = {6, 2}
# # d = a ^ b ^ c
# d = a.symmetric_difference(b).symmetric_difference(c)
# print(d)

# a = {1, 2}
# b = {3}
# c = {4, 5}
# d = {3, 2, 6}
# e = {6}
# f = {7, 8}
# g = {9, 8}
# al = a | b | c | d | e | f | g
# print(al)
# print("unic elems count:", len(al))
# print("max =", max(al))
# print("min =", min(al))

# a = "Hello"
# b = "How are you"
# c = set(a) & set(b)
# # print(c)
# for i in c:
#     print(i, end=" ")

# s = frozenset([1, 2, 3, 4, 5, 6])
# print(s)
# s1 = frozenset("hello")
# print(s1)


# Словарь (dict)

# lst = ["one", "two"]
# d = {"first": "one", "second": "two"}
# print(lst[1])
# print(d["second"])

# d = {0: "text", "one": 45, (1, 2): "Кортеж", True: [5, 9, 8, 7, 7], False: "один",
#      1: "Список"}  # ключом может быть Неизменяемый тип
# # данных
# print(d)

# d = {"first": "one", "second": "two"}    # можно использовать любые неизменяемые значения
# print(d)
# print(type(d))
# d1 = dict(first="one", second="two")    # можно использовать только строковые(str) значения!!!!!
# print(d1)
# print(type(d1))

# lst = [
#     ["one", 1],
#     ["two", 2],
#     ["three", 3]
# ]
#
# print(lst)
# d = dict(lst)
# print(d)

# d = {i: i ** 2 for i in range(1, 7)}
# print(d)
#
# for i in d:
#     print("Ключи", i, "value =", d[i])

# d = {"x1": 3, "x2": 7, "x3": 5, "x4": -1}
# res = 1
# for key in d:
#     res *= d[key]
#
# print(res)

# d = {"x1": 3, "x2": 7, "x3": 5, "x4": -1}
# print(d)
# del d["x2"]
# print(d)

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# print(d)

# d = {i: input("-> ")for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)

# goods = {
#     "1": ['Core-i3-4330', 9, 4500],
#     "2": ['Core-i3-4670k', 3, 8500],
#     "3": ['AMD FX-6300', 6, 3700],
#     "4": ['Pentium G3220', 8, 2100],
#     "5": ['Core-i5-4350', 5, 6500],
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input("№: ")
#     if n == "0":
#         break
#     else:
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Количество: "))
#                     goods[n][1] += count
#                     break
#                 except ValueError:
#                     print("Значение некорректно. Введите число")
#         else:
#             print("Такого ключа не существует")
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")

# print(dir(dict))

# d = {1: "one", 2: "two", 3:"three"}
# print(d.keys())
# print(d.values())
# print(d.items())
# for i, j in d.items():
#     print(i, ":", j)

# d = {1: "one", 2: "two", 3:"three"}
# d2 = d.copy()
# print("D =", d)
# print("D2 =", d2)
#
# d2[2] = "four"
# print("D =", d)
# print("D2 =", d2)

# d = {1: "one", 2: "two", 3: "three"}
# print(d)
# # d.clear()
# item = d.pop(3, "Элемент")
# print(d)
# print(item)

# d = {1: {11: "one", 2: "two", 3: "three"}}
# print(d)

# d = {1: "one", 2: "two", 3: "three"}
# print(d)
# # d.clear()
# # item = d.pop(3, "Элемент")
# item = d.popitem()
# print(d)
# print(item)

# d = {1: "one", 2: "two", 3: "three"}
# value = d[2]
# value = d.get(6)
# print(value)
# item = d.setdefault((4,"four"))
# print(d)
# print(item)

# d = {1: "one", 2: "two", 3: "three"}
# # a = {10: "A", 20: "B"}
# a = [(10, "A"), (20, "B"), (2, "C")]
# # c = d | a
# c = d.update(a)
# print(d)


# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# new_d = dict()
# # new_d['name'] = d.pop('name')
# # new_d['salary'] = d.pop('salary')
#
# print(d)
# print(new_d)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# d['location'] = d.pop('city')
# print(d)

# sales_data = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#               "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#               "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#               "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}
#
# for x, y in sales_data.items():
#     print(x)
#     for i, j in y.items():
#         print("\t", i, ":", j)


# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# new_d = {value: key for key, value in d.items()}
# print(d)
# print(new_d)


# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# new_d = {value: key for key, value in d.items() if value <= 2}
# print(new_d)

# d = {i: i * 5 for i in [10, 20, 30, 40, 50]}
# print(d)
#
# s = "Hello"
# d1 = {key: key * 3 for key in s}
# print(d1)

# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
#
# print(list(d.values()))
# print(list(d.keys()))
# print(list(d.items()))

# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
# s = None
# d = dict()
#
# for i in a:
#     if type(i) is str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)

# ZIP
# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)

# a = [1, 2, 3, 4]
# b = ['one', 'two', 'three']
# d = {k: v for k, v in zip(a, b)}
# print(d)

# one = {'name': 'Igor', 'surname': 'Pavlov', 'job': 'Consultant'}
# two = {'name': 'Irina', 'surname': 'Vetrova', 'job': 'Manager'}
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)

# s = [(1, 'a'), (2, 'b'), (3, 'c')]
# a, b = zip(*s)
# print(a)
# print(b)

# letters = ['b', 'd', 'a', 'c']
# numbers = [4, 1, 3, 2]
# d = dict(zip(letters, numbers))
# print(d)
#
# data1 = list(zip(letters, numbers))
# print(data1)
# data1.sort()
# print(data1)
# d2 = dict(data1)
# print(d2)
# data2 = list(zip(numbers, letters))
# print(data2)
# data2.sort()
# print(data2)
# d3 = {v: k for k, v in data2}
# print(d3)

# letters = ['b', 'd', 'a', 'c']
# numbers = [4, 1, 3, 2]
#
# data = sorted(zip(letters, numbers))
# print(dict(data))

# one = {'один': 1, 'два': 2}
# two = {'три': 3, 'четыре': 4}
# print({**one, **two})
#
# for k, v in {**one, **two}.items():
#     print(k, "->", v)

# colors = ['red', 'green', 'blue']
# ind = 1
# for color in colors:
#     print(str(ind) + "-й цвет: " + color)
#     ind += 1
#
# print()
# for index, color in enumerate(colors, start=10):
#     print(str(index) + "-й цвет: " + color)
#
# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
#
# for i, (k, v) in enumerate(d.items(), 1):
#     print(i, ") ", k, ": ", v, sep="")

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(1, 2, 3, 'abc'))
# print(func())


# def summa(*params):
#     res = 0
#     for n in params:
#         res += n
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(summa(7, 8, 9))


# def to_dict(*args):
#     return {i: i for i in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict("grey", (2, 17), 3.11, -4))

# def average(*args):
#     sr = sum(args) / len(args)
#     print(sr)
#     res = []
#     for num in args:
#         if num < sr:
#             res.append(num)
#     return res
#
#
# print(average(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(average(3, 6, 1, 9, 5))

# def func(a, *args):
#     return a, args
#
#
# print(func(5))
# print(func(1, 2, 3, 4, 5))

# def scores(student, *score):
#     print("Student Name:", student)
#     for i in score:
#         print(i)
#
#
# scores("Igor", 100, 95, 88, 92, 99)
# scores("Ivan", 77, 32, 88)

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func(name="Irina"))

# def info(**data):
#     for k, v in data.items():
#         print(k, ":", v)
#     print()
#
#
# info(name="Irina", surname="Vetrova", age=22)
# info(name="Igor", phone=987654, email="igor@mail.ru", age=22)

# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_dict = {"one": "first"}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyes_color='grey')
# print(my_dict)

# def func(a, *args, **kwargs):
#     return a, args, kwargs
#
#
# print(func(1, 2, 3, 4, 5, 6, c=55, d=66, e=77))

# def func1(*args):
#     print(args[0])
#
#
# def func2(**kwargs):
#     print(kwargs["one"])
#
#
# func1(1, 2, 3, 4, 5)
# func2(one=123, two=456)

# Области видимости (scope)

# name = "Tom"   #глобальная область видимости
#
#
# def hi():
#     global name
#     name = "Sam"
#     surname = "Jonson"  # локальная область видимости
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
#
# hi()
# bye()

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()


# import builtins
# name = dir(builtins)
# for t in name:
#     print(t)

# max = 5
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(max(lst))

# def add_two(a):
#     x = 2   # 2
#
#     def add_some():
#         print("x =", x)  # 4
#         return a + x       # 5
#
#     return add_some()   # 3    6
#
#
# print(add_two(3))   # 1    7


# Вложенные функции

# def outer(who):
#     def inner():
#         print("Hello,", who)
#
#     inner()
#
#
# outer("World")

# def outer():
#     a = 6
#
#     def inner(b):
#         a = 4
#         print("Сумма:", a + b)
#
#     print("a =", a)
#     inner(5)
#
#
# outer()

# x = 25

# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("a =", a)
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t
# print(c)

# x = 5
#
#
# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print("fn2.x =", x)
#
#     fn2()
#     print("fn1.x =", x)
#
#
# fn1()


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))


# def rect_paral(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + (inner(a, c) + inner(b, c)))
#     return s
#
#
# print(rect_paral(2, 4, 6))
# print(rect_paral(5, 8, 2))
# print(rect_paral(1, 6, 8))

# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# a = outer(5)
# print(a(10))
#
# b = outer(6)
# print(b(10))
#
# print(outer(5)(10))

# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "!"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
# res1()
# res1()
# res1()
# res2 = func("Сочи")
# res2()
# res2()
# res1()


# Анонимные функции (lambda)

# def func(x, y):
#     return x + y
#
#
# print(func(1, 2))
#
# print((lambda x, y: x + y)(1, 2))
#
# func1 = lambda x, y: x + y
#
# print(func1(1, 2))
# print(func1(5, 2))

# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c=3: a + b + c)(10, 20))
# print((lambda a, b=2, c=3: a + b + c)(10))
# print((lambda a=1, b=2, c=3: a + b + c)())

# print((lambda *args: sum(args))(1, 2, 3, 4, 5, 6, 7))
# print((lambda *args: sum(args))(6, 7))

# print((lambda **kwargs: sum(kwargs.values()))(a=1, b=2, c=3))

# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
# for t in c:
#     print(t("abc__"))


# def outer(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# f = outer(42)
# print(f(3))
#
#
# def outer(n):
#     return lambda x: x + n
#
#
# f = outer(42)
# print(f(3))
#
# outer = lambda n: lambda x: x + n
# f = outer(42)
# print(f(3))
#
# f = (lambda n: lambda x: x + n)(42)
# print(f(3))
#
# print((lambda n: lambda x: x + n)(42)(3))

# f = (lambda x: lambda y: lambda z: x + y + z)
# print(f(2)(4)(6))


# d = {'b': 10, 'a': 15, 'c': 4}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# d2 = dict(lst)
# print(d2)


# def func(i):
#     return i[1]
#
#
# d = {'b': 10, 'a': 15, 'c': 4}
# lst = list(d.items())
# print(lst)
# lst.sort(key=func)
# print(lst)
# d2 = dict(lst)
# print(d2


# players = [
#     {'name': "Антон", 'last name': 'Бирюков', 'rating': 9},
#     {'name': "Алексей", 'last name': 'Бодня', 'rating': 10},
#     {'name': "Федор", 'last name': 'Сидоров', 'rating': 4},
#     {'name': "Михаил", 'last name': 'Семенов', 'rating': 6},
# ]
#
# res1 = sorted(players, key=lambda item: item["last name"])
# print(res1)
#
# res2 = sorted(players, key=lambda item: item["rating"], reverse=True)
# print(res2)
#
# res3 = sorted(players, key=lambda item: item["rating"])
# print(res3)

# lst = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
#
# print(lst[0](12, 2))
# print(lst[1](12, 2))
# print(lst[2](12, 2))
# print(lst[3](12, 2))

# d = {
#     1: lambda: print("Январь"),
#     2: lambda: print("Февраль"),
#     3: lambda: print("Март"),
#     4: lambda: print("Апрель"),
#     5: lambda: print("Май"),
#     6: lambda: print("Июнь"),
#     7: lambda: print("Июль"),
#     8: lambda: print("Август"),
#     9: lambda: print("Сентябрь"),
#     10: lambda: print("Октябрь"),
#     11: lambda: print("Ноябрь"),
#     12: lambda: print("Декабрь"),
# }
# d[3]()

# map()

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# print(list(map(mult, lst)))
#
# print(list(map(lambda t: t * 2, lst)))
# print(list(map(lambda t: t * 2, [2, 8, 12, -5, -10])))
# lst1 = [2, 8, 12, -5, -10]
# lst2 = [3, 5, 7, 9, -11]
# print(dict(map(lambda x, y: (x, y), lst1, lst2)))
# print(list(map(lambda x, y: (x, y), lst1, lst2)))

# t = (2.88, -1.78, 100.55)
#
# print(tuple(map(lambda x: int(x), t)))
# print(tuple(map(int, t)))

# areas = [3.564789, 5.589614, 4.0123456, 56.875463, 9.4588745, 32.6523568]
# print(list(map(round, areas, range(1, 7))))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: x + y, l1, l2)))

# filter()

# t = ('abcd', 'qwe', 'zxcvb', 'def', 'hjk')
#
# print(tuple(filter(lambda s: len(s) == 3, t)))

# lst = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# print(list(filter(lambda s: s > 75, lst)))

# from random import randint
#
# lst = [randint(1, 30) for i in range(10)]
# print(list(filter(lambda s: 10 <= s <= 20, lst)))

# nums = [45, 55, 60, 37, 100, 105, 220]
# print(list(filter(lambda s: s % 15 == 0, nums)))
# print(list(filter(lambda s: not s % 15, nums)))

# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10)))))
#
# print([x ** 2 for x in range(10) if x % 2])

# Декораторы

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# text = hello
# print(text())

# def my_decorator(func):      # Декорирующая функция
#     def inner():
#         print("До кода")
#         func()
#         print("После кода")
#     return inner
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()

# def my_decorator(func):
#     def inner():
#         print("До кода")
#         func()
#         print("После кода")
#     return inner
#
#
# @my_decorator      # Декоратор
# def func_test():   # Декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# func_test()

# lst = [input('-> ') for i in range(5)]
# print(lst)
# num = list(map(int, lst))
# print(num)

# def my_decorator(func):
#     def inner():
#         print("До кода")
#         func()
#         print("После кода")
#     return inner
#
#
# @my_decorator      # Декоратор
# def func_test():   # Декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# func_test()

# def my_decorator(func):      # Декорирующая функция
#     def inner():
#         print("До кода")
#         func()
#         print("После кода")
#     return inner
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()
#
#
# def my_decorator(func):
#     def inner():
#         print("До кода")
#         func()
#         print("После кода")
#     return inner
#
#
# @my_decorator      # Декоратор
# def func_test():   # Декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# func_test()
# def circle(fn):
#     def wrap():
#         return "(" + fn() + ")"
#
#     return wrap
#
#
# def angle(fn):
#     def wrap():
#         return "<" + fn() + ">"
#
#     return wrap
#
#
# @angle
# @circle
# def expression():
#     return '5 + 2'
#
#
# print(expression())
# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count = count + 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def outer(fn):
#     def inner(arg1, arg2):
#         print("Данные:", arg1, arg2)
#         fn(arg1, arg2)
#
#     return inner
#
# @outer
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Ветрова")

# def outer(fn):
#     def inner(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return inner
#
#
# @outer
# def print_data(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, end="\n\n")
#
#
# print_data("Борис", "Елизавета", "Светлана", study="JavaScript")
# print_data("Владимир", "Екатерина", "Виктор")
# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)
# def multiply(arg):
#     def my_decorator(func):
#         def wrap(*args, **kwargs):
#             return arg * func(*args, **kwargs)
#
#         return wrap
#     return my_decorator
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) is not args[i]:
#                     raise TypeError("Неверный тип данных")
#             for k in kwargs:
#                 if type(f_kwargs[k]) is not kwargs[k]:
#                     raise TypeError("Неверный тип данных")
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Hello"))
# print(typed_fn2("Hello", " world", "!"))
# print(typed_fn3("Hello", " world", z=5))
# print(typed_fn3("Hello", " world", z="!"))

# Строки

# print(bin(18))   # 0b10010 - двоичная система счисления
# print(oct(18))   # 0o22 - восьмеричная система счисления
# print(hex(18))   # 0x12 - шестнадцатеричная система счисления
#
# print(0b10010)
# print(0o22)
# print(0x12)

# q = "Pyt"
# w = "hon"
# e = q + w
# print(e)
# # print(e * 3)
# # print("y" in e)
# # print("a" in e)
# print(e[1])
# print(e[::-1])
# def change_char_to_str(s, old, new):
#     s2 = ""
#     i = 0
#     while i < len(s):
#         if s[i] == old:
#             s2 += new
#         else:
#             s2 += s[i]
#         i += 1
#
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# str2 = change_char_to_str(str1, "N", "P")
# print(str1)
# print(str2)
# print(u"Привет")


# print("C:\\file.txt")
# print(r"C:\file.txt\\"[:-1])
# print(r"C:\file.txt" + "\\")
# print("C:\\file.txt\\")

# name = "Дмитрий"
# age = 25
# print(f"Меня зовут {name}. Мне {age} лет.")
# x = 10
# y = 5
# print(f"{x=}, {y=}")
# print(f"{10/7:.2f}")
# num = 74
# print(f"{{{num}}}")

# dir_name = "folder"
# file_name = "file.txt"
# print(fr"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" + file_name)
# s = """Многострочный
# текст
# """
# print(s)

# def square(n):
#     return n ** 2
#
#
# print(square(5))
#
# max()
# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания.
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord('a'))

# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# st = "Test string for me"
# arr = [ord(x) for x in st]
# print("ASCII коды", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1])-1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(35))
# print(chr(8364))

# a = 122
# b = 97
# for i in range(b, a + 1):
#     print(chr(i), end=" ")

# from random import randint
#
# SHORT = 8
# LONG = 16
# MIN_ASCII = 33
# MAX_ASCII = 123
#
#
# def random_password():
#     result = ""
#     rand_len = randint(SHORT, LONG)
#     for i in range(rand_len):
#         result += chr(randint(MIN_ASCII, MAX_ASCII))
#     return result


# print("Случайный пароль:", random_password())

# print(dir(str))

# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())
# print(s.lower())
# print(s.upper())
# print(s.swapcase()) # инвертирование регистра символов
# print(s.title())
# print(s.count("h", 1))
# print(s.lower().count("i"))
# print(s.find("Python"))     # возвращает первый индекс подстроки
# print(s.find("h", 1, -4))   # если вхождение не найдено, то возвращается "-1"
# st = "один два"
# one = st[:st.find(" ")]
# two = st[st.find(" ") + 1:]
# print(two + " " + one)

# print(s.rfind("h", 1, -4))   # возвращает последний индекс подстроки, если не найдено то "-1"
# print(s.rindex("h", 1, -4))

# st = "I am learning Python. Hello, WORLD"
# print(st[:st.find('h')] + st[st.rfind('h') + 1:])
# print(s.startswith("he"))    # возвращает TRUE если строка начинается с заданной подстроки
# print(s.startswith("I am", 14))
# print(s.find("I am"))
#
# print(s.endswith("Python"))   # возвращает TRUE если строка заканчивается с заданной подстроки

# print('abc123'.isalnum())   # проверяет состоит ли строка из букв и цифр
# print('abc%123'.isalnum())
#
# print("ABCsvb".isalpha())   # определяет состоит ли строка только из букв
#
# print("45612".isdigit())     # определяет состоит ли строка только из цифр

# print("abc".islower())      # проверяет состоит ли строка в нижнем регистре, допускается любые символы
# print("Abc".islower())
# print("a!@#$%%bc".islower())
#
# print("ABC".isupper())      # проверяет строку состоит ли она в верхнем регистре, допускается любые символы
# print("ABC!@#$%%^".isupper())
#
# print('py'.center(10))
# print('py'.center(10, "-"))
# print('py'.center(1))

# print("     py".lstrip())       # удаляет пробелы слева
# print("py    ".rstrip())       # удаляет пробелы справа
# print("     py    ".strip())       # удаляет пробелы
#
# print("https://www.python.org".lstrip("https:/"))
# print("https://www.python.org".rstrip("org."))
# print("https://www.python.org".strip("https:/org."))

# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# print(str1.replace("Nython", "Python", 2))    # поиск и замена

# st = "-"
# seq = ("a", "b", "c")
# print(st.join(seq))
#
# print("..".join(['1', '99']))
# print(":".join('abc'))
# print(":".join('a'))
#
# print("Строка разделенная пробелами".split())   # строку преобразует в список по символу разделителю
# print("www.python.org".split("."))
# print("www.python.org".split(".", 2))
#
# print("www.python.org".rsplit("."))
# print("www.python.org".rsplit(".", 2))

# st = "Никонов Валерий Анатольевич"
# st = input("Введите ФИО: ").split()
# print(st)
# print(f"{st[0]} {st[1][0]}. {st[2][0]}.")

# num = input("Введите числа через пробел: ").split()
# print(num)
# num = list(map(int, num))
# print(num)
# print(sum(num))


# Регулярные выражения
# import re


#
# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта.6789."
# reg = r"\."
# print(re.findall(reg, s))       # список, содержащий все совпадения
# print(re.search(reg, s))        # местоположение первого объекта
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
# print(re.match(reg, s))         # поиск совпадения только с начала строки
# print(re.split(reg, s))         # список, в котором строка разбита по заданному шаблону
# print(re.sub(reg, "!", s))

# print(dir(re))

# reg = r"[2025]"
# reg = r"[0-9]"
# reg = r"[а-я]"
# reg = r"[0-9]."
# reg = r"\d"
# reg = r"\D"
# reg = r"\s"
# reg = r"\S"
# reg = r"\w"
# reg = r"\W"
# reg = r"\w+"
# reg = r"\d*"
# reg = r"\d?"
# print(re.findall(reg, s))

# + - от 1 до бесконечности
# * - от 0 до бесконечности
# ? - от 0 до до 1 повторения

# st = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# reg = "[0-2][0-9]:[0-9][0-9]"
# print(re.findall(reg, st))

# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта.6789."
# d = "Цифры: 7, +17, -24, 0013, 0.3"
# reg = r"[+-]?[\d.]+"
# print(re.findall(reg, d))

# d = "05-03-1987  # Дата рождения"
#
# print("Дата рождения:", re.sub(r"\s\s#.+", "", d))
# print(re.sub("-", ".", re.sub(r"\s\s#.+", "", d)))

# st = "autor=Пушкин А.С.; title =Евгений Онегин; price =200; year= 1831"
# # reg = r"\w+\s*=\s*\w+\s*\w+\.?\w?\.?"
# # reg = r"\w+\s*=[\w\s.]*"
# reg = r"\w+\s*=[^;]+"
# print(re.findall(reg, st))
#
# reg1 = r"; "
# print(re.split(reg1, st))

# st = "12 сентября 2025 года"
# # reg = r"\d{4}"
# # reg = r"\d{2,4}"
# reg = r"\d{,4}"
# print(re.findall(reg, st))

# st = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 7494564578"
# reg = r"\+?7\d{10}"
# print(re.findall(reg, st))
# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта.6789. [Hel-lo] Wor_ld 200000000000"
# # reg = r"^\w+\s\w+"
# reg = r"\w+\s\w+$"
# print(re.findall(reg, s))


# def validate_login(login):
#     return re.findall(r"^[A-Za-z0-9_-]{3,16}$", login)
#
#
# print(validate_login("Python_master"))
# print(validate_login("Pyt"))

# text = "<body>Пример жадного совпадения соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))

# *?, +?, ??
# {m,n}?, {,n}?, {m,}?

# st = "Петр, Ольга и Виталий отлично учатся!"
# reg = r"Петр|Ольга|Виталий|Наталья"
# print(re.findall(reg, st))

# st = "int = 4, float = 4.0f, double = 8.0"
# # reg = r"\w+\s*=\s*\d[.\w+]*"
# # reg = r"int\s*=\s*\d[.\w+]*|float\s*=\s*\d[.\w+]*"
# # reg = r"(?:int|float)\s*=\s*\d[.\w+]*"
# reg = r"((int|float)\s*=\s*(\d[.\w+]*))"
# print(re.findall(reg, st))

# d = "Word2016, PS6, AI5"
# reg = r"([A-Za-z]+)(\d+)"
# print(re.findall(reg, d))

# st = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, st))

# s = "Самолет прилетает 10/23/2025. Будем рады вас видеть после 10/24/2025."
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))

# s = "yandex.com and yandex.ru"
# reg = r"(([a-z0-9-]{2,}\.)+[a-z]{2,4})"
# print(re.sub(reg, r"http://\1", s))

# s = "28-08-2021"
# reg = r"^([0][0-9]|[12][0-9]|3[01])-([0][1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])$"
# print(re.findall(reg, s))

# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))

# text = "hello world"
# print(re.findall(r"\w+", text))
# print(re.findall(r"\w+", text, re.DEBUG))

# Рекуксия

# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)
#     print(n, end=" ")
#
#
# n1 = int(input("На каком этаже вы находитесь: "))
# elevator(n1)

# def sum_list(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# def to_str(n, base):
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(254, 16))
#
# names = ["adam", ["bob", ["chet", "cat"], "barb", "bert"], "alex", ["bea", "bill"], "ann"]
# print(len(names))
# print(names[0].title())
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))

# names = ["adam", ["bob", ["chet", "cat"], "barb", "bert"], "alex", ["bea", "bill"], "ann"]


# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))


# Файлы

# f = open(r"C:\Python522\text.txt", 'r')
# print(f)
# print(*f)
# f.close()
# print(f.closed)

# file = "text2.txt"
# f = open(file, "w")
# f.write("Замена строки в текстовом файле;"
#         "\nИзменить строку в списке;"
#         "\nЗаписать список в файл;\n")
# f.close()
#
# f = open(file)
# data = f.readlines()
# print(data)
# data[1] = "Hello World!\n"
# print(data)
# f.close()
#
# f = open(file, "w")
# f.writelines(data)
# f.close()

# f = open('text3.txt', "w")
# lst = [i for i in range(1, 100, 5)]
# print(lst)
# for index in lst:
#     f.write(str(index) + "\t")
# f.close()

# f = open("text.txt")
# print(f.read(3))
# print(f.tell()) # возвращает условную позицию в файле
# print(f.seek(1))    # перемещает условный курсор в заданную позицию
# print(f.read())
# f.close()

# f = open("text.txt", "r+")
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()

# f = open("text.txt", "a+")
# print(f.read())
# f.close()

# with open("text.txt", "w") as f:
#     print(f.write("0123456789"))
# print(f.closed)
#
# with open("text.txt") as f:
#     print(f.read())

# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 5.47]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return " ".join(lt)
#
#
# with open("res.txt", "w") as f:
#     f.write(get_line(lst))
#
# print("Файл записан")

# with open("res.txt") as f:
#     nums = f.read()
#
# print(nums)
#
# lst = list(map(float, nums.split()))
# print(lst)
# print(sum(lst))

# file_name = "long.txt"
# with open(file_name, "w") as f:
#     f.write("Файл — именованная область данных на носителе информации, используемая как базовый объект"
#             "  с данными в операционных системах.") # взаимодействия
#
#
# def longest_word(file):
#     with open(file) as text:
#         lst = text.read().split()
#         print(lst)
#         max_length = len(max(lst, key=len))
#         print(max_length)
#         res = [word for word in lst if len(word) == max_length]
#
#         return res[0] if len(res) == 1 else res
#
#
# print(longest_word(file_name))

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10
# \n"
# with open("one.txt", "w") as f:
#     f.write(text)
#
# with open("one.txt", "r") as fr, open("two.txt", "w") as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)

# Модули OS и OS.PATH

# import os

# print(os.getcwd())   # путь к текущей директории
# print(os.listdir())     # список директорий и файлов
# print(os.listdir(".venv"))

# os.mkdir("folder")      # создали папку
# os.rmdir("folder")      # удалили папку

# os.makedirs("nested1/nested2/nested3/")     # создается папка с промежуточными директориями
# os.remove("xyz.txt")    # удаляет файл
# os.rename("file_name", "file_name.txt") # переименовывает файл либо перемещает в существующую директорию

# with open("text1.txt", "w+") as f:
#     f.write("Hello")
#     f.seek(0)
#     data = f.read()
#     data += "!"
#     f.write(data)

# print("Данные в локальном репозитории")
# print("Hello")


# dirs = [r'Work\F1', r'Work\F2\F21']
#
# # for d in dirs:
# #     os.makedirs(d)
#
# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }

# for key, value in files.items():
#     for file in value:
#         file_path = os.path.join(key, file)
#         open(file_path, "w").close()


# file_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
# for file in file_with_text:
#     with open(file, 'w', encoding="utf-8") as f:
#         f.write(f"Некоторый текст для файла {file}")

# def print_tree(topdown):
#     print(f"Обход Work {'сверху вниз'if topdown else 'снизу вверх'}")
#     for root, directory, file in os.walk("Work", topdown):
#         print(root)
#         print(directory)
#         print(file)
#     print("-" * 50)
#
#
# print_tree(False)
# print_tree(True)


# Work\w.txt
# Work\F1\f11.txt
# Work\F1\f12.txt
# Work\F1\f13.txt
# Work\F2\F21\f211.txt
# Work\F2\F21\f212.txt

# import os
# import time
#
# path = "main.py"
# print(os.path.getsize(path))    # размер файла
# print(os.path.getatime(path))   # время последнего доступа к файлу в секундах
# print(os.path.getmtime(path))   # время последнего изменения файла
# print(os.path.getctime(path))       # время создания файла
#
# size = os.path.getsize(path)
# a_time = os.path.getatime(path)
# m_time = os.path.getmtime(path)
# c_time = os.path.getctime(path)
#
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(a_time)))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(m_time)))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(c_time)))
# print(size)
# print(size // 1024)

# import os
#
# file_path = r"C:\Python522\Book1.py"
# if os.path.exists(file_path):
#     directory, file = os.path.split(file_path)
#     a_time = os.path.getatime(file_path)
#     print(f"{file} ({directory}) - {a_time}")
# else:
#     print(f"Фйл {file_path} не существует")
# import os
#
# dir_name = "Work"
#
# objs = os.listdir(dir_name)
# print(objs)
#
# for obj in objs:
#     p = os.path.join(dir_name, obj)
#     # print(p)
#     if os.path.isfile(p):
#         print(f"{obj} - file - {os.path.getsize(p)} bytes")
#     if os.path.isdir(p):
#         print(f"{obj} - dir")

# import os
#
#
# def info_files(root, folder):
#     for root, dirs, files in os.walk(root):
#         for file in files:
#             file_path = os.path.join(root, file)
#             # print(file_path)
#             file_size = os.path.getsize(file_path)
#             if file_size == 0:
#                 os.renames(file_path, os.path.join(folder, file))
#                 print(f"Файл {file} перемещен из папки {root} в папку {folder}")
#             else:
#                 print(f"{file_path} - {file_size} bytes")
#
#
# info_files("Work", "Work/empty_files")

# ООП (объектно ориентированное программирование)

# class Point:
#     x = 1
#     y = 2


# p1 = Point()
# # Point.x = 100
# # print(p1.x)
# # print(Point.x)
# # print(id(p1))
# # print(id(Point))
# p1.x = 100
# p1.y = 50
# print(p1.x, p1.y)
# print(p1.__dict__)
#
# p2 = Point()
# print(p2.x, p2.y)
# print(p2.__dict__)
# print(Point.__dict__)

# class Point:
#     x = 1
#     y = 2
#
#     def set_coord(self):
#         print(self.__dict__)
#
#
# p1 = Point()
# p1.x = 5
# p1.y = 10
# p1.set_coord()
# Point.set_coord(p1)
#
# p2 = Point()
# p2.set_coord()

# class Point:
#     x = 1
#     y = 2
#
#     def set_coord(self, x1, y1):
#         self.x = x1
#         self.y = y1
#
#
# p1 = Point()
# p1.set_coord(5, 10)
# Point.set_coord(p1, 10 , 20)
# print(p1.__dict__)
#
# p2 = Point()
# p2.set_coord(2, 7)
# print(p2.__dict__)

# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}
#         \nСтрана: {self.country}"f"\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва","Чистопрудный бульвар 1А")
# h1.print_info()
# h1.set_name("Юлия")
# h1.print_info()
# print(h1.get_name())

# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __del__(self):
#         print("Удаление экземпляра")
#
#     def print_info(self):
#
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника", self.skill, "\n")
#
#
# p1 = Person("Виктор", "Резник")
# p1.print_info()
# p1.add_skill(3)
#
# p2 = Person("Анна", "Долгих")
# p2.print_info()
# p2.add_skill(2)

# class Person:
#     count = 0
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         Person.count += 1
#
#     def print_info(self):
#         print("Данные сотрудника:", self.name, self.surname)
#
#
# p1 = Person("Виктор", "Резник")
# p1.print_info()
#
#
# p2 = Person("Анна", "Долгих")
# p2.print_info()
# print(p1.count)
# print(p2.count)
# print(Person.count)

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(f"{self.name} выключается")
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(f"{self.name} был последним")
#         else:
#             print(f"Работающих роботов осталось: {Robot.k}")
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
# droid3 = Robot("C-3P2")
# droid3.say_hi()
# print("Численность роботов:", Robot.k)
# print("\nЗдесь роботы могут проделать какую то работу.\n")
# print("Роботы закончили свою работу. Давайте их выключим.\n")
# del droid1, droid2, droid3
# print("Численность роботов:", Robot.k)

# class Point:
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#     def set_coord_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coord_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#
# p1 = Point(5, 10)
# # print(p1.__x, p1.__y)
# # p1.z = 20
# # p1.__x = 100
# # p1.__y = "abc"
# # print(p1.__x, p1.__y)
# p1.set_coord(5.2, 100)
# p1.set_coord_x(8.2)
# print(p1.get_coord())
# print(p1.__dict__)
# # p1.__check_value(10)
# # print(Point.__dict__)
# p1._Point__x = 111
# print(p1._Point__x)
# print(p1.__dict__)
# import math
#
# class Rectangle:
#     def __init__(self, length=1, width=1):
#         self.__length = length
#         self.__width = width
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     def get_width(self):
#         return self.__width
#
#     def get_length(self):
#         return self.__length
#
#     def set_width(self, width):
#         if Rectangle.__check_value(width):
#             self.__width = width
#
#     def set_length(self, length):
#         if Rectangle.__check_value(length):
#             self.__length = length
#
#     def get_area(self):
#         return self.__width * self.__length
#
#     def get_perimetr(self):
#         return (self.__width + self.__length) * 2
#
#     def get_hypotenuse(self):
#         return round(math.sqrt(self.__length ** 2 + self.__width ** 2), 2)
#
#     def get_draw(self):
#         for i in range(self.__length):
#             print("*" * self.__width)
#
#
# r1 = Rectangle()
# # r1.set_width("a")
# # r1.set_length(3)
# print("Длина прямоугольника:", r1.get_length())
# print("Ширина прямоугольника:", r1.get_width())
# print("Площадь прямоугольника:", r1.get_area())
# print("Периметр прямоугольника:", r1.get_perimetr())
# print("Гипотенуза прямоугольника:", r1.get_hypotenuse())
# r1.get_draw()

# class Point:
#     __slots__ = "x", "y"
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 10)
# # p1.z = 20
# print(p1.x, p1.y)
# # print(p1.x, p1.y, p1.z)
# # print(p1.__dict__)

# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     def __set_coord_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата х должны быть числом")
#
#     def __get_coord_x(self):
#         return self.__x
#
#     def __del_coord_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     coordX = property(__get_coord_x, __set_coord_x,__del_coord_x)
#
#
# p1 = Point(5, 10)
# p1.coordX = 20.5
# print(p1.coordX)
# del p1.coordX
# print(p1.__dict__)

# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата х должны быть числом")
#
#     @x.deleter
#     def x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     # coordX = property(__get_coord_x, __set_coord_x, __del_coord_x)
#
#
# p1 = Point(5, 10)
# p1.x = 50
# print(p1.x)
# del p1.x
# print(p1.__dict__)

# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.__old = old
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# p1 = Person("Irina", 26)
# print(p1.__dict__)
# p1.name = "Igor"
# p1.old = 31
# print(p1.name)
# print(p1.old)
# del p1.name
# print(p1.__dict__)

# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(Point.get_count())

# def inc(x):
#     return x + 1
#
#
# def dec(x):
#     return x - 1
#
#
# print(inc(10), dec(10))
#
#
# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))

# class Numbers:
#     @staticmethod
#     def max(a, b, c, d):
#         mx = a
#         if b > mx:
#             mx = b
#         if c > mx:
#             mx = c
#         if d > mx:
#             mx = d
#         return mx
#
#     @staticmethod
#     def min(*args):
#         mn = args[0]
#         for i in args:
#             if i < mn:
#                 mn = i
#         return mn
#
#     @staticmethod
#     def average(*args):
#         return sum(args) / len(args)
#
#     @staticmethod
#     def factorial(n):
#         fact = 1
#         for i in range(1, n + 1):
#             fact *= i
#         return fact
#
#
# print(Numbers.max(3, 5, 7, 9))
# print(Numbers.min(3, 5, 7, 9))
# print(Numbers.average(3, 5, 7, 9))
# print(Numbers.factorial(5))

# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, string_date):
#         day, month, year = map(int, string_date.split("."))
#         date1 = cls(day, month, year)
#         return date1
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# # string_date = "23.10.2025"
# # day, month, year = map(int, string_date.split("."))
# # print(day, month, year)
# # date = Date(day, month, year)
# d1 = Date.from_string("23.10.2025")
# print(d1.string_to_db())
# d2 = Date.from_string("12.30.2024")
# print(d2.string_to_db())

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, num, surname, percent, value):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 44)
#
#     def __del__(self):
#         print("*" * 44)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print(f"Проценты были успешно начислены!")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#
# acc = Account("12345", "Долгих", 0.03, 1000)
# # acc.print_balance()
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
#
# acc.add_percents()
# print()
#
# acc.withdraw_money(100)
# print()
# acc.withdraw_money(3000)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letter = "".join(re.findall(r"[a-zа-яё-]", fio, flags=re.IGNORECASE))
#         for s in f:
#             # print(s.strip(letter))
#             if len(s.strip(letter)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 100:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 100 лет")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#
# p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.8)
# print(p1.__dict__)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self) -> str:
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#         print("Инициализатор класса Prop")
#
#
# class Line(Prop):
#
#     def __init__(self, *args):
#         print("Переопределенный инициализатор line")
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()


# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if not isinstance(w, int):
#             raise TypeError("Ширина должна быть числом")
#         elif not w > 0:
#             raise ValueError("Ширина должна быть положительным числом")
#
#         else:
#             self.__width = w
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if isinstance(h, int) and h > 0:
#             self.__height = h
#         else:
#             print("Высота должна быть положительным числом")
#
#     def get_area(self):
#         print(f"Площадь {self.color} прямоугольника: ", end="")
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, "green")
# print(rect.width)
# print(rect.height)
# print(rect.color)
# rect.width = -8
# rect.color = "red"
# print(rect.get_area())


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник:\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         self.fon = background
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, r_width, r_type, r_color):
#         super().__init__(width, height)
#         self.r_width = r_width
#         self.r_type = r_type
#         self.r_color = r_color
#
#     def show_rect(self):
#         super().show_rect()
#         print(f"Ширина рамки: {self.r_width}\nТип рамки: {self.r_type}\nЦвет рамки: {self.r_color}")
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, "1px", "solid", "blue")
# shape2.show_rect()
# from math import sqrt
#
#
# class Pair:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def edit_a(self, a):
#         self.a = a
#
#     def edit_b(self, b):
#         self.b = b
#
#     def sum(self):
#         return self.a + self.b
#
#     def mult(self):
#         return self.a * self.b
#
#
# class RightTriangle(Pair):
#     def __init__(self, a, b):
#         super().__init__(a, b)
#         self.c = self.hypotenuse()
#
#     def hypotenuse(self):
#         hypo = round(sqrt(self.a ** 2 + self.b ** 2), 2)
#         print(f"Гипотенуза ABC: {hypo}")
#         return hypo
#
#     def print_info(self):
#         print(f"Прямоугольный треугольник ABC: ({self.a}, {self.b}, {self.c})")
#
#     def square(self):
#         s = 0.5 * self.mult()
#         print(f"Площадь ABC: {s}")
#
#     def edit_a(self,a):
#         super().edit_a(a)
#         self.c = self.hypotenuse()
#
#     def edit_b(self,b):
#         super().edit_b(b)
#         self.c = self.hypotenuse()
#
#
# tr = RightTriangle(5, 8)
# tr.print_info()
# tr.square()
# print()
# print(f"Сумма: {tr.sum()}")
# print(f"Произведение: {tr.mult()}")
# print()
# tr.edit_a(10)
# tr.edit_b(20)
# print(f"Сумма: {tr.sum()}")
# print(f"Произведение: {tr.mult()}")
# tr.square()

# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))

# Перегрузка методов

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coord(self, x=None, y=None):
#         if y is None:
#             self.x = x
#         elif x is None:
#             self.y = y
#         else:
#             self.x = x
#             self.y = y
#
#
# p1 = Point(5, 7)
# print(p1.__dict__)
# p1.set_coord(20, 30)
# print(p1.__dict__)
# p1.set_coord(50)
# print(p1.__dict__)
# p1.set_coord(y=100)
# print(p1.__dict__)

# Абстрактные методы

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self) -> str:
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def draw(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     def draw(self):
#         print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 20)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(70, 70), Point(90, 90)))
#
# for f in figs:
#     f.draw()

# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную доску")
#
#     @abstractmethod
#     def move(self):
#         print("Метод move() в базовом классе")
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещен на е2е4")
#
#
# # q = Chess()
# q = Queen()
# q.draw()
# q.move()

# from math import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self.width = self.length = width
#             else:
#                 self.width = width
#                 self.length = length
#         else:
#             self.radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод calc_area()")
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self.width * self.length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self.radius ** 2, 2)
#
#
# t = SqTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t2 = SqTable(20)
# print(t2.__dict__)
# print(t2.calc_area())
#
# t1 = RoundTable(radius=20)
# print(t1.__dict__)
# print(t1.calc_area())

# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     suffix = "RUB"
#
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=" ")
#
#     def print_info(self):
#         self.print_value()
#         print(f" = {self.convert_to_rub():.2f} {Currency.suffix}")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end="")
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end="")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# print("*" * 50)
# for elem in d:
#     elem.print_info()
# print("*" * 50)
# for elem in e:
#     elem.print_info()
# for elem in d:
#     elem.print_value()
#     print(f" = {elem.convert_to_rub():.2f} RUB")
# print()
#
# for elem in e:
#     elem.print_value()
#     print(f" = {elem.convert_to_rub():.2f} RUB")

# Интерфейс

# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Child class")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("GrandChild class")
#
#
# gc = GrandChild()
# gc.display1()
# gc.display2()

# Вложенные классы

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def outer_static_method():
#         print("Метод внешнего класса")
#
#     def outer_obj_method(self):
#         print("Метод внешнего экземпляра класса", self.name)
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Метод вложенного класса", MyOuter.age, self.obj.name)
#             MyOuter.outer_static_method()
#             self.obj.outer_obj_method()
#
#
# out = MyOuter("внешний")
# out.outer_obj_method()
# inner = out.MyInner("внутренний", out)
# print(out.name)
# print(inner.inner_name)
# inner.inner_method()


# class Color:
#     def __init__(self):
#         self.name = "green"
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = "light Green"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Color()
# outer.show()
# print(outer.name)
# # print(outer.lg.name)
# # outer.lg.display()
# g = outer.lg
# g.display()

# class Intern:
#     def __init__(self):
#         self.name = "Дмитрий"
#
#     def display(self):
#         print("name:", self.name)
#
#
# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = Intern()
#         # self.head = self.Head()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class Head:
#         def __init__(self):
#             self.name = "Александр"
#
#         def display(self):
#             print("name:", self.name)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# # d2 = outer.head
# # d1 = Employee().Intern()
# d2 = Employee().Head()
# d1.display()
# d2.display()

# class Outer:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print("Наружный класс")
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print("Промежуточный класс")
#
#         class InnerClass:
#             def show(self):
#                 print("Вложенный класс")
#
#
# outer = Outer()
# outer.show()
#
# inner1 = outer.inner
# inner1.show()
#
# inner2 = outer.inner.inner_inner
# inner2.show()

# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i9"
#
#
# comp = Computer()
# my_os = comp.os
# my_cpu = comp.cpu
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())


# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print("In base class")
#
#     class Inner:
#         def display1(self):
#             print("Inner of base class")
#
#
# class SubClass(Base):
#     def __init__(self):
#         print("In Subclass")
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print("Inner of Subclass")
#
#
# a = SubClass()
# # a.display()
# # b = a.db
# b = SubClass.Inner()
# b.display1()
# b.display2()

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
#
#
# dog = Dog("Buddy")
# dog.sleep()
# dog.play()
# dog.bark()

# class A:
#     def __init__(self):
#         print("Инициализатор класса А")
#
#
# class AA:
#     def __init__(self):
#         print("Инициализатор класса АA")
#
#
# class B(A):
#     def __init__(self):
#         print("Инициализатор класса B")
#
#
# class C(AA):
#     def __init__(self):
#         print("Инициализатор класса C")
#
#
# class D(B, C):
#     def __init__(self):
#         print("Инициализатор класса D")
#
#
# d = D()
# print(D.mro())
# # print(D.__mro__)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Styles:
#     def __init__(self, color="red", width=1):
#         print("Инициализатор Styles")
#         self.color = color
#         self.width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print("Инициализатор Pos")
#         self.sp = sp
#         self.ep = ep
#         Styles.__init__(self, *args)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f"Рисование линии: {self.sp}, {self.ep}, {self.color}, {self.width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# l1.draw()

# Миксины

# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename="logfile.txt"):
#         with open(filename, "a") as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=""):
#         super().log(message, filename="log.txt")
#
#
# subclass = MySubClass()
# subclass.display("Эта строка будет печататься и записываться в файл")

# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init MixinLog")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 15:20")
#
#
# class Notebook(Goods, MixinLog):
#     ...
#
#
# notebook = Notebook("HP", 1.5, 35000)
# notebook.print_info()
# notebook.save_sell_log()

# Перегрузка операторов
# Число секунд в одном дне: 24 * 60 = 86400

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         # if self.sec == other.sec:
#         #     return True
#         # return False
#         return self.sec == other.sec
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#
# c1 = Clock(100)
# c2 = Clock(100)
# # c4 = Clock(300)
# # c1 += c2
# # c3 = c1 + c2 + c4
# print(c1.get_format_time())
# print(c2.get_format_time())
# # print(c3.get_format_time())
# if c1 == c2:
#     print("Время одинаковое")
# else:
#     print("время разное")

# class Student:
#     def __init__(self, name, *marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым положительным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#         del self.marks[key]
#
#
# s1 = Student("Сергей", 5, 5, 3, 4, 5)
# print(s1[2])
# s1[10] = 4
# del s1[2]
# print(s1.marks)

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#         if item == "hour":
#             return (self.sec // 3600) % 24
#         if item == "min":
#             return (self.sec // 60) % 60
#         if item == "sec":
#             return self.sec % 60
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом")
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#
#         if key == "hour":
#             self.sec = s + 60 * m + value * 3600
#         if key == "min":
#             self.sec = s + 60 * value + h * 3600
#         if key == "sec":
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(8000)
# print(c1.get_format_time())
# print(c1["hour"], c1["min"], c1["sec"])
# c1["hour"] = 10
# c1["min"] = 62
# c1["sec"] = 70
# print(c1.get_format_time())

# class Point:
#     def __init__(self, x):
#         self.x = x
#
#     def __str__(self):
#         return f"{self.x}"
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.x}"
#
#
# p1 = Point(5)
# print(p1)
# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy!!!"
#         elif self.pol == "F":
#             return f"{self.name} is good girl!!!"
#         else:
#             return f"{self.name} is good kitty!!!"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age={self.age}, pol='{self.pol}')"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat("No name", 0, choice(["M", "F"])) for _ in range(1, randint(2, 6))]
#         else:
#             raise TypeError("Types are not supported!")
#
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Elsa", 5, "F")
# # cat3 = Cat("Murzik", 3, "R")
# print(cat1)
# print(cat2)
# print(cat1 + cat2)

# class Point:
#     def __init__(self, *args):
#         self.__coord = args
#
#     def __len__(self):
#         return len(self.__coord)
#
#
# p = Point(1, 2, 3)
# print(len(p))
# import math
#
#
# class Point:
#     __slots__ = ("x", "y", "__length")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#     @property
#     def length(self):
#         return self.__length
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p1 = Point(1, 2)
# print(p1.length)

# class Point:
#     __slots__ = ("x", "y")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt1 = Point(1, 2)
# pt2 = Point2D(1, 2)
# print("pt1 =", pt1.__sizeof__())
# print("pt2 =", pt2.__sizeof__() + pt2.__dict__.__sizeof__())

# class Point:
#     __slots__ = ("x", "y")
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = ("z",)
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# p = Point(1, 2)
# p3 = Point3D(10, 20, 30)
# p3.z = 30
# print(p3.z)

# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))
#
#
# t1 = Number(10)
# t2 = Text("Python")
# print(t1.total(35))
# print(t2.total(35))

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Cat(Animal):
#     def info(self):
#         print(f"Я кот. Меня зовут {self.name}. Мой возраст {self.age}.")
#
#     def make_sound(self):
#         print(f"{self.name} мяукает.")
#
#
# class Dog(Animal):
#     def info(self):
#         print(f"Я собака. Меня зовут {self.name}. Мой возраст {self.age}.")
#
#     def make_sound(self):
#         print(f"{self.name} гавкает.")
#
#
# cat = Cat("Пушок", 2.5)
# dog = Dog("Мухтар", 4)
#
# for animal in cat, dog:
#     animal.info()
#     animal.make_sound()


# Функторы

# class Counter:
#     def __init__(self):
#         self.__count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Counter()
# c1()

# def string_strip(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return string.strip(chars)
#
#     return wrap
#
#
# s1 = string_strip("?:!.; ")
# print(s1("   Hello world!  .... "))
#
#
# class StringStrip:
#     def __init__(self, chars):
#         self.chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return args[0].strip(self.chars)
#
#
# s2 = StringStrip("?:!.; ")
# print(s2("   Hello world!  .... "))

# class MyDecorator:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self):
#         print("Перед вызовом функции")
#         self.func()
#         print("После вызова функции")
#
#
# @MyDecorator
# def func():
#     print("text")
#
#
# func()


# class MyDecorator:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self, a, b):
#         # print("Перед вызовом функции")
#         res = self.func(a, b)
#         # print("После вызова функции")
#         return f"Перед вызовом функции\n{res}\nПосле вызова функции"
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# print(func(2, 5))

# class Power:
#     def __init__(self, fn):
#         self.fn = fn
#
#     def __call__(self, a, b):
#         return self.fn(a, b) ** 2
#
#
# @Power
# def mult(a, b):
#     return a * b
#
#
# print(mult(2, 3))

# class MyDecorator:
#     def __init__(self, fn):
#         self.func = fn
#
#     def __call__(self, *args, **kwargs):
#         res = self.func(*args, **kwargs)
#
#         return f"Перед вызовом функции\n{res}\nПосле вызова функции"
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# @MyDecorator
# def func1(a, b, c):
#     return a * b * c
#
#
# print(func(2, 5))
# print(func1(2, 5, 2))

# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, fn):
#         def wrap(*args, **kwargs):
#             res = fn(*args, **kwargs)
#
#             return f"Перед вызовом функции\n{self.name}\n{res}\nПосле вызова функции"
#
#         return wrap
#
#
# @MyDecorator("test2")
# def func(a, b):
#     return a * b
#
#
# print(func(2, 5))

# class MyDecorator:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, fn):
#         def wrap(*args, **kwargs):
#             res = fn(*args, **kwargs)
#             return f"Результат: {res ** self.name}"
#
#         return wrap
#
#
# @MyDecorator(3)
# def func(a, b):
#     return a * b
#
#
# print(func(2, 2))

# Декорирование методов

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()


# Декораторы класса

# def decorator(cls):
#     class Wrapper(cls):
#         def sample(self, value):
#             return value * 2
#
#     return Wrapper
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Init ActualClass")
#
#     def method_in_class(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.method_in_class(4))
# print(obj.sample(4))

# Матаклассы

# a = 5
# print(type(a))
# print(type(int))

# class MyList(list):
#     def get_length(self):
#         return len(self)

# MyList = type(
#     'MyList',
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
#
# lst = MyList()
# lst.append(5)
# lst.append(7)
# print(lst, lst.get_length())

# Создание модулей

# import geometry.rect
# import geometry.sq
# import geometry.trian
# from geometry import rect, sq, trian

# from geometry import *
# if __name__ == "__main__":
#
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.get_perimeter())

# from car.electro_car import ElectroCar
#
# if __name__ == "__main__":
#     e_car = ElectroCar("Tesla", "T", 2018, 99000, 100)
#     e_car.show_car()
#     e_car.description_battery()

# Упаковка (Сериализация) и распакковка (Десериализация) данных
# import pickle

# filename = "basket.txt"
# shop = {
#     "фрукты": ["яблоко", "груша"],
#     "овощи": ("морковь", "лук"),
#     "бюджет": 1000
# }
#
# with open(filename, "wb") as fh:
#     pickle.dump(shop, fh)
#
# with open(filename, "rb") as fh:
#     shop_list = pickle.load(fh)
#
# print(shop_list)

# class Test:
#     num = 25
#     string = "Привет"
#     lst = [1, 2, 3]
#     dictionary = {"first": 1, "second": 2}
#
#     def __str__(self):
#         return f"Число: {Test.num}\nСтрока: {Test.string}\nСписок: {Test.lst}\nСловарь: {Test.dictionary}"
#
#
# obj = Test()
# # print(obj)
#
# obj1 = pickle.dumps(obj)
# print(f"Сериализация в строку:\n{obj1}\n")
#
# obj2 = pickle.loads(obj1)
# print(f"Десериализация из строки:\n{obj2}\n")

# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     # def __str__(self):
#     #     return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr["c"]
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# print(item1)
# item2 = pickle.dumps(item1)
# print(item2)
# item3 = pickle.loads(item2)
# print(item3)
# print(item3.__dict__)

# data = {
#     'name': "Olga",
#     'age': 35,
#     20: None,
#     True: False,
#     'hobbies': ('running', 'singing'),
#     'children': [
#         {'firstname': 'Alice',
#          'age': 6}
#     ]
#
# }
# with open('data_file.json', 'w') as fw:
#     json.dump(data, fw, indent=4)
#
# with open('data_file.json', "r") as fw:
#     data1 = json.load(fw)
#
# # print(data1)
#
# json_string = json.dumps(data, skipkeys=True)
# print(json_string)

# x = {"name": "Виктор"}
#
# print(json.dumps(x))
# print(json.dumps(x, fw))
#
# a = json.dumps(x)
# print(json.load(a))
#
# with open("data_file1.json", "w") as fw:
#     json.dump(x, fw, ensure_ascii=False)

# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'k', 'l', 'm', 'n']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#     # print(name)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open("persons.json"))
#     except FileNotFoundError:
#         data = []
#     data.append(person_dict)
#     with open("persons.json", "w") as f:
#         json.dump(data, f, indent=2)
#
#
# # persons = []
# # for i in range(5):
# #     persons.append(gen_person())
# # print(gen_person())
#
# for i in range(5):
#     write_json(gen_person())
# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         # st = ''
#         # for i in self.marks:
#         #     st += str(i) + ", "
#         # return f"Студент => {self.name}: {st[:-2]}"
#         st = ", ".join(map(str, self.marks))
#         return f"Студент => {self.name}: {st}"
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_marks(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     def dump_to_json(self):
#         data = {"name": self.name, "marks": self.marks}
#         with open(self.get_file_name(), "w") as f:
#             json.dump(data, f)
#
#     def get_file_name(self):
#         return self.name + ".json"
#
#     def load_from_file(self):
#         with open(self.get_file_name(), "r") as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         st = "\n".join(map(str, self.students))
#         return f"\nГруппа: {self.group}\n{st}"
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_group(gr1, gr2, index):
#         return gr2.add_student(gr1.remove_student(index))
#
#     def get_file_name(self):
#         return self.group.lower().replace(" ", "-") + ".json"
#
#     def dump_to_json(self):
#         data = [{'name': student.name, 'marks': student.marks} for student in self.students]
#         with open(self.get_file_name(), "w") as f:
#             json.dump(data, f, indent=2)
#
#     def load_from_file(self):
#         with open(self.get_file_name(), "r") as f:
#             print(json.load(f))
#
#
# st1 = Student("Bodnya", [5, 4, 3, 4, 5, 3])
# # print(st1)
# # st1.add_mark(4)
# # print(st1)
# # st1.delete_mark(3)
# # print(st1)
# # st1.edit_marks(2, 4)
# # print(st1)
# # print(st1.average_mark())
# st2 = Student("Nikolaenko", [2, 3, 5, 4, 2])
# st3 = Student("Birukov", [3, 5, 3, 2, 5, 4])
# st1.dump_to_json()
# st1.load_from_file()
#
# sts1 = [st1, st2]
# group1 = Group(sts1, "ГК Python")
# # print(group1)
# # # print()
# # group1.add_student(st3)
# # # print(group1)
# # # print()
# # group1.remove_student(1)
# # # print(group1)
# sts2 = [st2]
# group2 = Group(sts2, "ГК Web")
# # print(group1)
# # print(group2)
# Group.change_group(group1, group2, 0)
# print()
# print(group1)
# print(group2)
# group2.dump_to_json()
# group2.load_from_file()

# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
# # print(todos)
#
# todos_by_user = {}
# for todo in todos:
#     if todo["completed"]:
#         try:
#             todos_by_user[todo["userId"]] += 1
#         except KeyError:
#             todos_by_user[todo["userId"]] = 1
#
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
#
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
#
# # users = ["11"]
# print(users)
#
# max_users = " and ".join(users)
# print(max_users)
#
# e = "s" if len(users) > 1 else ""
# print(f"user{e} {max_users} completed {max_complete} TODOs")


# import json
#
#
# class CountryCapital:
#     @staticmethod
#     def add_country(file_name):
#         new_country = input("Введите название страны: ").lower()
#         new_capital = input("Введите название столицы: ").lower()
#
#         try:
#             data = json.load(open(file_name, encoding="utf-8"))
#         except FileNotFoundError:
#             data = {}
#
#         data[new_country] = new_capital
#
#         with open(file_name, "w", encoding="utf-8") as f:
#             json.dump(data, f, indent=2, ensure_ascii=False)
#
#     @staticmethod
#     def load_from_file(file_name):
#         with open(file_name, encoding="utf-8") as f:
#             print({k.capitalize(): v.capitalize() for k, v in json.load(f).items()})
#
#     @staticmethod
#     def delete_country(file_name):
#         del_country = input("Введите название страны: ").lower()
#
#         try:
#             data = json.load(open(file_name, encoding="utf-8"))
#         except FileNotFoundError:
#             data = {}
#
#         if del_country in data:
#             del data[del_country]
#
#             with open(file_name, "w", encoding="utf-8") as f:
#                 json.dump(data, f, indent=2, ensure_ascii=False)
#         else:
#             print("Такой страны в базе нет")
#
#     @staticmethod
#     def search_data(file_name):
#         country = input("Введите название страны: ").lower()
#         try:
#             data = json.load(open(file_name, encoding="utf-8"))
#         except FileNotFoundError:
#             data = {}
#
#         if country in data:
#             print(f"Страна {country.title()} столица {data[country].title()} есть в словаре")
#         else:
#             print(f"Страны {country.title()} нет в словаре")
#
#     @staticmethod
#     def edit_data(file_name):
#         country = input("Введите страну для корректировки: ").lower()
#         new_capital = input("Введите новое название столицы: ").lower()
#         try:
#             data = json.load(open(file_name, encoding="utf-8"))
#         except FileNotFoundError:
#             data = {}
#
#         if country in data:
#             data[country] = new_capital
#
#             with open(file_name, "w", encoding="utf-8") as f:
#                 json.dump(data, f, indent=2, ensure_ascii=False)
#         else:
#             print("Такой страны в базе нет")
#
#
# file = "list_capital.json"
# while True:
#     index = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных"
#                   "\n4 - редактирование данных""\n5 - просмотр данных\n6 - завершение работы\nВвод: ")
#     if index == "1":
#         CountryCapital.add_country(file)
#     elif index == "2":
#         CountryCapital.delete_country(file)
#     elif index == "3":
#         CountryCapital.search_data(file)
#     elif index == "4":
#         CountryCapital.edit_data(file)
#     elif index == "5":
#         CountryCapital.load_from_file(file)
#     elif index == "6":
#         break
#     else:
#         print("Введен некорректный номер")
#
#     print("*" * 50)

# import csv

# with open("data.csv") as f:
#     fields = ["Имя", "Профессия", "Год рождения"]
#     file_reader = csv.DictReader(f, delimiter=";", fieldnames=fields)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"\t{row["Имя"]} - {row["Профессия"]}. Родился в {row["Год рождения"]} году.")
#         count += 1
#     print(f"Всего в файле {count} строки.")

# with open("data.csv") as f:
#     file_reader = csv.DictReader(f, delimiter=";")
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(row)
#         count += 1
#     print(f"Всего в файле {count} строки.")

# import csv

# with open("students.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", "9", "15"])
#     writer.writerow(["Саша", "5", "12"])
#     writer.writerow(["Маша", "11", "18"])

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open("sw_data.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)
#
# with open("sw_data.csv", "r") as f:
#     print(f.read())

# import csv

# with open("stud.csv", "w") as f:
#     names = ["Имя", "Возраст"]
#     file_writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=names)
#     file_writer.writeheader()
#     file_writer.writerow({"Имя": "Саша", "Возраст": 6})
#     file_writer.writerow({"Имя": "Маша", "Возраст": 15})
#     file_writer.writerow({"Имя": "Вова", "Возраст": 14})

# import csv
#
# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open("dict_writer.csv", "w") as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=data[0].keys())
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)

# import sqlite3

# con = sqlite3.connect("profile.db")
# cur = con.cursor()
#
# cur.execute("""""")
#
# con.close()

# with sqlite3.connect("profile.db") as con:
#     cur = con.cursor()
#     cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     summa REAL,
#     date BLOB
#     )""")
#     cur.execute("DROP TABLE users")

# import sqlite3
#
# with sqlite3.connect("users.db") as con:
#     cur = con.cursor()
# cur.execute("""
# CREATE TABLE IF NOT EXISTS person(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
#  name TEXT NOT NULL,
#  phone BLOB NOT NULL DEFAULT "+79097654321",
#  age INTEGER CHECK(age > 0 AND age < 100),
#  email TEXT UNIQUE
#  )
#  """)
# cur.execute("""
# ALTER TABLE person
# RENAME TO person_table;
# """)
#
# cur.execute("""
#     ALTER TABLE person_table
#     ADD COLUMN address TEXT
#     """)

# cur.execute("""
#         ALTER TABLE person_table
#         RENAME COLUMN address TO home_address
#         """)

# cur.execute("""
#             ALTER TABLE person_table
#             DROP COLUMN home_address
#             """)

# cur.execute("""
#                 DROP TABLE person_table
#
#                 """)

# with sqlite3.connect("db_3.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     SELECT *
#     FROM T1
#     LIMIT 2, 5
#     """
#                 )
#
# # for res in cur:
# #     print(res)
# # res = cur.fetchall()
# # print(res)
# # res2 = cur.fetchmany(2)
# # print(res2)
# #
# # res1 = cur.fetchone()
# # print(res1)
#
# from bs4 import BeautifulSoup

# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find("div", class_="row")
# row = soup.find_all("div", class_="row")[2].find("div", class_="name").text
# row = soup.find_all("div", class_="row")[2].find("div", {"data-set": "salary"})
# row = soup.find_all("div", class_="row")[2].find("div", {"class": "name"})
# row = soup.find("div", string="Alena").parent
# row = soup.find("div", string="Alena").find_parent(class_="row")
# row = soup.find("div", id="whois3").find_next_sibling()
# print(row)


# def get_copywriter(tag):
#     whois = tag.find("div", class_="whois").text
#     if "Copywriter" in whois:
#         return tag
#     return None
#
#
# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
#
# copywriter = []
# row = soup.find_all("div", class_="row")
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
#
# print(copywriter)
# import re
#
#
# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
# salary = soup.find_all("div", {"data-set": "salary"})
# for i in salary:
#     get_salary(i.text)

# from bs4 import BeautifulSoup
# import requests


# r = requests.get("https://ru.wordpress.org/")
# print(r.headers['content-type'])
# print(r.content)
# print(r.text)
# from bs4 import BeautifulSoup
# import requests
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find("h1", class_="wp-block-heading").text
#     return p1
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     print(get_data(get_html(url)))
#
#
# if __name__ == "__main__":
#     main()

# from bs4 import BeautifulSoup
# import requests
# import re
# import csv
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refind(s):
#     return re.sub(r"\D+", "", s)
#
#
# def write_csv(data):
#     with open('plagins.csv', "a") as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow([data["name"], data["url"], data["rating"], data["snippet"]])
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("section", class_="plugin-section")[2]
#     plugins = p1.find_all("li")
#     for plugin in plugins:
#         name = plugin.find("h3", class_="entry-title").text
#         url = plugin.find("h3", class_="entry-title").find("a").get("href")
#         rating = plugin.find("span", class_="rating-count").text
#         replace_rating = refind(rating)
#         snippet = plugin.find("div", class_="entry-excerpt").text.strip()
#         data = {"name": name, "url": url, "rating": replace_rating, "snippet": snippet}
#         write_csv(data)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == "__main__":
#     main()

# from bs4 import BeautifulSoup
# import requests
#
# r = requests.get("https://ru.wordpress.org/")
# print(r.headers['content-type'])
# print(r.content)
# print(r.text)

# from bs4 import BeautifulSoup
# import requests
# import csv
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refind(s):
#     return s.split()[-1]
#
#
# def write_csv(data):
#     with open('plugins_list.csv', 'a', encoding="UTF-8") as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow([data['name'],
#                          data['url'],
#                          data['active'],
#                          data['tested']])
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("li", class_="wp-block-post")
#     for el in p1:
#         name = el.find("h3", class_="entry-title").text
#         url = el.find("h3", class_="entry-title").find("a")["href"]
#         active = el.find("span", class_="active-installs").text.strip()
#         try:
#             texted = el.find("span", class_="tested-with").text.strip()
#             test = refind(texted)
#         except AttributeError:
#             test = ""
#         data = {
#             'name': name,
#             'url': url,
#             'active': active,
#             'tested': test
#         }
#         write_csv(data)
#
#
# def main():
#     for i in range(1, 50):
#         url = f"https://ru.wordpress.org/plugins/browse/popular/page/{i}/"
#         get_data(get_html(url))
#
#
# if __name__ == "__main__":
#     main()

from parsers import Parser


def main():
    pars = Parser('https://www.ixbt.com/live/index/news/', 'news.txt')
    pars.run()


if __name__ == '__main__':
    main()
