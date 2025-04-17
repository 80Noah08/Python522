class Human:
    def __init__(self, fio, old):
        self.fio = fio
        self.old = old


class Student(Human):
    def __init__(self, fio, old):
        super().__init__(fio, old)
        self.count = count
        self.group = group

    def student_info(self, group, count):
        self.group = group
        self.count = count
        super().__init__(fio, old)
        


class Graduate(Student):
    def graduate_info(self, work):
        super().student_info(group, count)
        self.work = work


class Teacher(Human):
    def teach_info(self, lesson):
        self.lesson = lesson


st1 = [ Student("Батодалаев Даши", 16), Student.student_info( "ГК Web_011", 5)]
