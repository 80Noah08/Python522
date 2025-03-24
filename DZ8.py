# from random import randint
#
#
# def res():
#     tpl1 = tuple(randint(0, 5) for i in range(10))
#     tpl2 = tuple(randint(-5, 0) for i in range(10))
#     new_tpl = tpl1 + tpl2
#     print("кортеж-1", tpl1, "\nКортеж-2", tpl2, "\nОбъединение кортежей", new_tpl)
#     print("0 =", new_tpl.count(0))
#
#
# res()

#!!!!!!!!!!!!!!!!Вариант учителя


from random import randint


def ran(a, b):
    return tuple(randint(a, b) for i in range(10))


tpl1 = ran(0, 5)
print(tpl1)
tpl2 = ran(-5, 0)
print(tpl2)
tpl3 = tpl1 + tpl2
print(tpl3)
print("0 =", tpl3.count(0))