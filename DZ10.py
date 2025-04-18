# Запрашиваем кол-во студентов для проверки
col_students = int(input("Введите кол-во студентов: "))

# Создаем словарь для хранения введенных данных и их последующего использования
data = {input(str(i + 1) + "-й студент: "): int(input("Бал студента: ")) for i in range(col_students)}
print(data)

# Задаем условие для нахождения среднего арифметического
sr = round(sum(data.values()) / col_students)
print("Средний бал:", sr, "\nСтуденты с баллом выше среднего:")

# Прогоняем полученные данные через цикл для вывода студентов с балом выше среднего
for i in data:
    if data[i] > sr:
        print(i)