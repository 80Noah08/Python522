# first_name = ("Кичигин")
# name = ("Артём")
# second_name = ("Иванович")
#
# age = ("возвраст: 29 лет")
#
# print(first_name)
# print(name)
# print(second_name)
# print(age)
from sys import excepthook

# my_age = 100
# if my_age >= 100:
#     print("Сто лет! Впечатляет.")
# elif my_age <= 3:
#     print("Оууу. Совсем малыш.")
# else:
#     print('эх, какой хороший возвраст.')


# favorite_team = 'Викинги'
# if not favorite_team == 'Викинги':
#     print("не повезло")
# else:
#     print('вперед викинги')


# favs = ['Raf', 'Leo']
# if 'Mikye' in favs and 'Dony'in favs:
#     print('Круто!')
# elif 'Mikye' in favs or 'Dony' in favs:
#     print('мне он тоже нравится')
# else:
#     print("мне они не нравятся")


# Введите пятизначное число: 97531
# произведение чисел: 97531: 945
# среднее арифметическое: 5.0

# num = 4321
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)


# num1 = float(input("Введите число: "))
# num2 = float(input("Введите число: "))
# num3 = float(input("Введите число: "))
# num4 = float(input("Введите число: "))
# a = num1 + num2
# b = num3 + num4
# c = a / b
# print(round(c, 2))

# num = int(input("Введите пятизначное число "))
# res = num % 10 * 10000     #
# num //= 10
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Домашнее задание номер 2!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# num = int(input("Введите пятизначное число "))
# a = num % 10
# b = int(num % 100)
# b //= 10
# c = int(num % 1000)
# c //= 100
# d = int(num % 10000)
# d //= 1000
# e = int(num % 100000)
# e //= 10000
# x = a * b * c * d * e
# s = (a + b + c + d + e) / 5
# print("Произведение цыфр:", x)
# print("Среднее значение:", s)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# n = 1
# if n % 10 == 1:
#     print(n, "копейка")
# elif 2 <= n % 10 <= 4:
#     print(n, "копейки")
# else:
#     print(n, "копеек")

# n = int(input("Введите число от 1 до 99: "))
# a = n % 10
# if 1 == a and n != 11:
#     print(n, "копейка")
# elif 2 <= a <= 4 and n != 12 and n != 13 and n != 14:
#     print(n, "копейки")
# else:
#     print(n, "копеек")


# name = input("Введите имя: ")
# b = int(input("Введите баланс: "))
# if name == "Art" and b <= 1000:
#     print("Имя пользователя:", name,   "\nБаланс: ", b)
# elif name == "Pyt" and b >= 1000:
#     print("Имя пользователя:", name, "\nБаланс: ", b,)
# else:
#     print("Неправильно указано имя или баланс")


# m = input("Введите тип материала книга/видео: ")
# if m == "книга" or m == "видео":
#     print("Материал добавлен: тип - ", m)
# else:
#     print("неправильно выбран материал")
# s = int(input("Введите стоимость материала: "))
# if 100 <= s <= 1000:
#     print("Стоимость - ", s)
# else:
#     print("неправильно указана стоимость")
# kat = input("Введите категорию материала: ")
# if kat == "математика" or kat == "история":
#     print("Категория - ", kat)
# else:
#     print("неправильно выбрана категория")

# m = input("Введите тип материала книга/видео: ")
# s = int(input("Введите стоимость материала: "))
# kat = input("Введите категорию материала: ")
# if m == "видео" or "книга" and 100<= s <= 1000 and kat == "математика" or "история":
#     print("материал добавлен: тип - ", m, ",",  "стоимость - ", s, ",",  "категория - ", kat)
# else:
#     print("неправильно введены данные")

# a = int(input("Введите свой возраст: "))
# if 0 <= a <= 99:
#     print("")
#     if a >= 16:
#         print("Вы можете получить права!")
#     else:
#         print("Вы слишком молоды :)")
# else:
#     print("неправильно указан возраст")

# a = int(input("Введите свой возраст: "))
# if 0 <= a <= 99:
#     print("")
#     if 0 <= a <= 4:
#         print("Билет бесплатный")
#     elif 5 <= a <= 17:
#         print("Стоимость билета: 10 дол.")
#     else:
#         print("Стоимость билета: 20 дол.")
# else:
#     print("неправильно указан возраст")

# s = int(input("Введите сумму покупки: "))
# b = int(input("Введите свой возраст: "))
# if 0 <= s <= 1000 and 0 <= b <= 99:
#     print("Cумма покупки: ", s,  end="")
#     if s >= 100 and b >= 65:
#         print("\nВаша скидка составляет - 15% \nСпасибо за покупку!")
#     elif s >= 100:
#         print("\nВаша скидка составляет - 10% \nСпасибо за покупку!")
#     elif 0 < s < 100 and b >= 65:
#         print(" Ваша скидка составляет 5% \nСпасибо за покупку!")
#     elif 0 < s < 100 or 0 <= b < 65:
#         print("\nСпасибо за покупку! ")
# else:
#     print("Неправильно указана сумма покупки или возраст")


# a = 1
# while a <= 10:
#     print(a)
#     a += 1

# for number in range(1, 11):
#     if number == 5:
#         break
#     print(number)

# for number in range(1, 11):
#     if number == 5:
#         continue
#     print(number)

# try:
#     res = int(input("Введите число: "))
# except ValueError:
#     print("Это не число!")
# else:
#     print(f"Вы ввели число - ", res)


# while True:
#     try:
#         number_of_transaction = int(input("Введите кол-во транзакций, которое вы хотите добавить: "))
#         if number_of_transaction >= 0:
#             break
#         else:
#             print("Кол-во транзакций не может быть отрицательным. Попробуйте снова.")
#     except ValueError:
#         print("Неверный ввод! Пожалуйста, введите число.")
#
# for i in range(number_of_transaction):
#     while True:
#         try:
#             amount = float(input("Введите сумму транзакции: "))
#             if amount >= 0:
#                 break
#             else:
#                 print("Сумма не может быть отрицательной. Пожалуйста, введите положительное значение.")
#         except ValueError:
#             print("Неверный ввод! Пожалуйста, введите числовое значение суммы.")
# description = input("Введите описание транзакции: ")
# print(f"Введена транзакция: Сумма - {amount}, Описание - '{description}")
#
# print("\nВсе транзакции успешно введены.")

# while True:
#     try:
#         number_of_day = int(input("Введите кол-во дней для учета расходов на обед: "))
#         if number_of_day >= 0:
#             break
#         else:
#             print("Кол-во дней не может быть отрицательным. Попробуйте снова.")
#     except ValueError:
#         print("Пожалуйста, введите число.")
#
# for i in range(1, number_of_day, +1):
#     while True:
#         try:
#             expense = float(input(f"Введите расходы на обед за день {i}: "))
#             if expense >= 0:
#                 break
#             else:
#                 print("Расходы не могут быть отрицательными. Пожалуйста, введите положительное значение")
#         except ValueError:
#             print("Неверный ввод! Пожалуйста, введите числовое значение расходов.")
#     print(f"За день {i} зарегистрированы расходы на обед в размере {expense} рублей.")
#
# print("\nВсе расходы на обеды успешно зарегистрированы.")


# def hello(name, age):
#     print("Меня зовут:", name, "\nМой возраст:", age)
#
#
# hello("Irina", 28)


# def get_sum(a, b):
#     print(a + b)
#
#
# get_sum(2, 3)


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
# print(maximum(9, 15))

# def res(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
#
# x = int(input("Введите первое значение: "))
# y = int(input("Введите второе значение: "))
# print(res(x, y))


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
#     print("Второе число больше первого")
# print(one_big(10, 5))
# print(one_big(10, 15))


# data = {}
# col_students = int(input("Введите кол-во студентов: "))
# for keys in data:
#     name_student = input("Введите имя студента: ")
#     for values in data[keys]:
#         bal_student = int(input("Введите балл студента(цифрой): "))
#
#     print(data)

col_students = int(input("Введите кол-во студентов: "))
d = {input("Введите имя студента: "): int(input("Введите балл студента: ")) for i in range(col_students)}
print(d)
for ind in enumerate(d, 1):
    print(str(ind) + "-й студент: ")
sr = sum(d.values()) / col_students
print("Средний бал:", sr, "\nСтуденты с баллом выше среднего:")
for i in d:
    if d[i] > sr:
        print(i)
