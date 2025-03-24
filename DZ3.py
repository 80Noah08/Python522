# n = int(input("Введите число от 1 до 99: "))
# if 0 <= n <= 99:
#     print(" ")
#     a = n % 10
#     if 1 == a and n != 11:
#         print(n, "копейка")
#     elif 2 <= a <= 4 and n != 12 and n != 13 and n != 14:
#         print(n, "копейки")
#     else:
#         print(n, "копеек")
# else:
#     print("неправильно указано число")


# a = int(input("Введите начало диапозона: "))
# b = int(input("Введите конец диапозона: "))
# res = 0
# while a <= b:
#     if a % 2:
#         print(a, end=" ")
#         res += a # res = res + a
#     a += 1
# print("\nСумма: ", res)


res = 0
while True:
    n = int(input("Введите число: "))
    if n == 0:
        break
    else:
        res += n
print("Результат: ", res)