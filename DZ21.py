
# """ Сделал два варианта, не знал какой отправить """

# """ Вариант №1 """


class Change:

    def __init__(self, kg=0):
        self.__kg = kg

    def __check_value(c):
        if isinstance(c, int) or isinstance(c, float):
            return True
        return False

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, kg):
        if Change.__check_value(kg):
            self.__kg = kg
            print(self.__kg, "кг =>", round(self.__kg * 2.20462, 2), "фунтов")
        else:
            print("Килограммы задаются только числами")


c1 = Change()
c1.kg = 12
c1.kg = 41
c1.kg = "abc"


# """ Я не понял как точно надо было ))) по записи урока вроде как вариант № 2, но первый мне больше нравится,
# более красивый что ли))) """

# """Вариант №2 """


class Change:

    def __init__(self, kg=12):
        self.__kg = kg

    def __check_value(c):
        if isinstance(c, int) or isinstance(c, float):
            return True
        return False

    @property
    def kg(self):
        return self.__kg

    @kg.setter
    def kg(self, kg):
        if Change.__check_value(kg):
            self.__kg = kg
        else:
            print("Килограммы задаются только числами")

    def change(self):
        return round(self.__kg * 2.20462, 2)


c1 = Change()
print(c1.kg, "кг =>", c1.change(), "фунтов")
c1.kg = 41
print(c1.kg, "кг =>", c1.change(), "фунтов")
c1.kg = "abc"
