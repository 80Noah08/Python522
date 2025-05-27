from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    @abstractmethod
    def print_info(self):
        pass

    def person_info(self):
        print(f"{self.surname} {self.name} {self.age} {self.print_info()}")


class Student(Human):
    def __init__(self, surname, name, age, study, group, average):
        super().__init__(surname, name, age)
        self.study = study
        self.group = group
        self.average = average

    def print_info(self):
        return f"{self.study} {self.group} {self.average}"


class Teacher(Human):
    def __init__(self, surname, name, age, discipline, skill):
        super().__init__(surname, name, age)
        self.discipline = discipline
        self.skill = skill

    def print_info(self):
        return f"{self.discipline} {self.skill}"


class Graduate(Student):
    def __init__(self, surname, name, age, study, group, average, project):
        super().__init__(surname, name, age, study, group, average)
        self.project = project

    def print_info(self):
        return f"{super().print_info()} {self.project}"


st1 = Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5)
st2 = Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5)
gr1 = Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных")
tch1 = Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110)
st3 = Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5)
tch2 = Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
lst = [st1, st2, gr1, tch1, st3, tch2]
for i in lst:
    i.person_info()
