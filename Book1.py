# message = "Hello Python world!"
# print(message)
#
# message = "Hello Python Crash course world!"
# print(message)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!! Методы строк(STR)!!!!!!!!!!!!!!
# name = "ada lovelace"
# print(name.title())       # метод .title заменяет начальные строчные символы на верхний регистр
# name = "Ada Lovelace"
# print(name.upper())      # метод .upper возводит все символы в верхний регистр
# print(name.lower())      # метод .lower возводит все символы в нижний регистр

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! f-string !!!!!!!!!!!!!!!!!!!!!!!!
# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"
# message = f"Hello, {full_name.title()}!"
# print(message)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Пробельные символы !!!!!!!!!!!!!!!!!
# print("Python")
# print("\tPython")     # "\t..." добавляют табуляцию(4 пробела)
# print("Languages:\nPython\nC\nJavaScript")    # "\n...." разрыв строк(начинает текст с новой строки)
# print("Languages:\n\tPython\n\tC\n\tJavaScript")

# favorite_message = "Python "
# print(favorite_message.rstrip())   # метод .rstrip удаляет лишний пробел справа
# favorite_message = " Python"
# print(favorite_message.lstrip())  # метод .lstrip удаляет лишний пробел слева
# favorite_message = " Python "
# print(favorite_message.strip())   # метод .strip удаляет лишний пробел с обеих сторон

# nostrach_url = 'https://nostrach.com'
# simple_url = nostrach_url.removeprefix('https://')   # .removeprefix удаляет префикс в скобках указывается что удалить
# print(simple_url)

# with_suf = 'python_notes.txt'
# simple_suf = with_suf.removesuffix('.txt')   #метод удаляет суффикс т.е расшиерние (txt)
# print(simple_suf)

# famous_person = " альберт эйнштейн "
# message = "<<Тот кто не совершал ошибок, никогда не пробовал что то нового>>."
# print(famous_person.title().strip(), "однажды сказал:", "\n", message, sep="")

# !!!!!!!!!!!!!!!!!!!!!!!!!!! Списки !!!!!!!!!!!!!!!!!!!!!!!!!!
# bicycles = ['trek', 'rocket', 'saturn']
# message = f"Мой первый велосипед: {bicycles[0].title()}"
# print(message)

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# motorcycles[0] = 'ducati'
# print(motorcycles)

# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles.append('ducati')    # .append добавляет новый элемент в конец списка
# print(motorcycles)

# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles.insert(0, 'ducati')   # .insert добавляет элемент в список на указанный индекс
# print(motorcycles)

# motorcycles = ['honda', 'yamaha', 'suzuki']
# del motorcycles[0]    # del удаляет элемент из списка по индексу
# print(motorcycles)

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# popped_motorcycles = motorcycles.pop()   # .pop удаляет элемент по индексу с возможностью сохранения
# print(motorcycles)
# print(f"Последний мотоцикл который я покупал был: {popped_motorcycles.title()}")

# motorcycles = ['ducati', 'honda', 'yamaha', 'suzuki']
# motorcycles.remove('ducati')   # .remove удаляет элемент списка по значению
# print(motorcycles)

# motorcycles = ['ducati', 'honda', 'yamaha', 'suzuki']
# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print(f"{too_expensive} is too expensive for me")

# cars = ['bmw', 'toyota', 'subaru', 'audi']
# print(cars)
# cars.sort()    # .sort сортирует элементы в списке по алфавиту (НАВСЕГДА)
# print(cars)
# cars.sort(reverse=True)    # .sort(reverse=True) сортирует список в обратном порядке по алфавиту(НАВСЕГДА)
# print(cars)

# cars = ['bmw', 'toyota', 'subaru', 'audi']
# print(f"Это исходный список машин: {cars}")
# print(f"Это отсортированный список машин: {sorted(cars)}") # sorted ВРЕМЕННО сортирует список

# cars = ['bmw', 'toyota', 'subaru', 'audi']
# cars.reverse()   # .reverse выводит список в обратном порядке (НАВСЕГДА)
# print(cars)

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")
# print("Thank you, everyone. That was a great magic show!")

# squares = []
# for value in range(1, 11):
#     square = value ** 2
#     squares.append(square)
# print(squares)

# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print("Here are the first three players on my team:")
# for player in players[:3]:
#     print(player.title())

my_food = ['pizza', 'falafel', 'carrot cake']
friend_food = my_food[:]
my_food.append('cannoli')
friend_food.append('ice cream')
print("My favorite foods are:")
print(my_food)
print("\n My friend's favorite foods are:")
print(friend_food)