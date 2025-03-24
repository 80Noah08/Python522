# with open("DZ_17.txt", "w") as file:
#     file.write("Замена строки в текстовом файле;"
#                "\nЗаписать список в файл;"
#                "\nИзменить строку в списке;\n")
#     st1 = "\nЗамена строки в текстовом файле;"
#     st2 = "\nЗаписать список в файл;"
#     st3 = "\nИзменить строку в списке;"
#
#     pos1 = int(input("pos1 = "))
#     pos2 = int(input("pos2 = "))
#     for pos1 in file:
#         if pos1 > st3:
#             print("Такой строки нет!")
#             break

file = "text2.txt"
f = open(file, "w")
f.write("Замена строки в файле;\n"
        "Изменить строку в списке;\n"
        "Записать список в файл;\n")
f.close()

f = open(file, "r")
read_line = f.readlines()
f.close()

pos1 = int(input("pos1 = "))
pos2 = int(input("Pos2 = "))

if 0 <= pos1 < len(read_line) and 0 < pos2 < len(read_line):
    read_line[pos1], read_line[pos2] = read_line[pos2], read_line[pos1]
else:
    print("Такой строки нет")
print(read_line)

f = open(file, "w")
f.writelines(read_line)
f.close()
