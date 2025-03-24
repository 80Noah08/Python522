s = 0
a = [0] * int(input("n = "))
for i in range(len(a)):
    a[i] = int(input(" -> "))
    if a[i] < 0:
        s += a[i]
print("Сумма отрицательных чисел: ", s)


# !!!!вариант преподователя!!!!
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# res = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         res += a[i]
# print(res)

# !!!!!Либо!!!!!

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# res = 0
# for i in a:
#     if i < 0:
#         res += i
# print(res)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]    # 3547

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []  # [2, 1, 4, 3]
#
# for i in a:  # 5
#     for j in b:  # 4
#         if i in c:
#             continue
#         if i == j:  # 5 == 4
#             c.append(i)
#             break
# print(c)

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]    # 3547
# print(a)
# for i in a:
#     while a.count(i) > 1:
#         a.remove(i)
# print(a)

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]    # 3547
#
# for i in a:
#     while a.count(i) != 1:
#         a.remove(i)
# print(a)

# 9