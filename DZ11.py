# # 1 вариант нахождение площади параллелепипеда
# def rect_parallelepiped(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + (inner(a, c) + inner(b, c)))
#     return s
#
#
# print(rect_parallelepiped(2, 4, 6))
# print(rect_parallelepiped(5, 8, 2))
# print(rect_parallelepiped(1, 6, 8))

# 2 вариант нахождение площади параллелепипеда с глобальной переменной S

# s = 0


# def rect_parallelepiped(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     global s
#     s = 2 * (inner(a, b) + (inner(a, c) + inner(b, c)))
#     return s
#
#
# print(rect_parallelepiped(2, 4, 6))
# print(rect_parallelepiped(5, 8, 2))
# print(rect_parallelepiped(1, 6, 8))

# 3 вариант нахождение площади параллелепипеда с локальной переменной S

# def rect_parallelepiped(a, b, c):
#     s = 0
#
#     def inner(i, j):
#         nonlocal s
#         s += i * j
#
#     inner(a, b)
#     inner(a, c)
#     inner(b, c)
#     s = 2 * s
#     return s
#
#
# print(rect_parallelepiped(2, 4, 6))
# print(rect_parallelepiped(5, 8, 2))
# print(rect_parallelepiped(1, 6, 8))
