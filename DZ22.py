# # Вариант №1
# import re
#
#
# class Account:
#     __slots__ = ["__surname", "__number", "__percent", "__balance"]
#     __usd_course = 0.012
#     __eur_course = 0.011
#     __rub = "RUB"
#     __usd = "USD"
#     __eur = "EUR"
#
#     def __init__(self, surname, number, percent, balance):
#         self.check_surname(surname)
#         self.check_number(number)
#         self.check_percent(percent)
#         self.check_money(balance)
#         self.__surname = surname
#         self.__number = number
#         self.__percent = percent
#         self.__balance = balance
#         print(f"Счёт #{self.__number} принадлежащий {self.__surname} был открыт.\n{"*" * 50}\n")
#
#     def __del__(self):
#         print(f"Счёт #{self.__number} принадлежащий {self.__surname} закрыт.\n{"*" * 50}")
#
#     @classmethod
#     def change_usd(cls, new_usd):
#         Account.check_money(new_usd)
#         cls.__usd_course = new_usd
#
#     @classmethod
#     def change_eur(cls, new_eur):
#         Account.check_money(new_eur)
#         cls.__eur_course = new_eur
#
#     @staticmethod
#     def converter(balance, exchange_rate):
#         return balance * exchange_rate
#
#     @staticmethod
#     def check_surname(surname):
#         if not isinstance(surname, str):
#             raise TypeError("Неверный тип данных при вводе фамилии")
#         if not re.fullmatch(r"^[a-zа-яё-]+$", surname, re.IGNORECASE):
#             raise ValueError("Некорректный ввод фамилии")
#
#     @staticmethod
#     def check_number(number):
#         if not isinstance(number, (str, int)):
#             raise TypeError("Некорректный тип данных для номера счёта")
#         if not re.fullmatch(r"^1\d{4,15}$", str(number)):
#             raise ValueError("Некорректный номер счёта")
#
#     @staticmethod
#     def check_percent(value):
#         if not isinstance(value, float):
#             raise TypeError("Некорректный тип данных для значения процента")
#         if value < 0 or value > 1:
#             raise ValueError("Некорректное значение величины процента")
#
#     @staticmethod
#     def check_money(money):
#         if not isinstance(money, (int, float)):
#             raise TypeError("Некорректный тип данных для произведения операции")
#         if money <= 0:
#             raise ValueError("Некорректное значение для произведения операции")
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, new_surname):
#         self.check_surname(new_surname)
#         self.__surname = new_surname
#
#     def withdrawal(self, money):
#         self.check_money(money)
#         if money > self.__balance:
#             print(f"К сожалению у вас нет {money} {Account.__rub} на счёте.\n{self.print_balance()}\n")
#         else:
#             self.__balance -= money
#             print(f"Было успешно снято {money} {Account.__rub}\n{self.print_balance()}\n")
#
#     def add_money(self, money):
#         self.check_money(money)
#         self.__balance += money
#         print(f"{money} {Account.__rub} было успешно добавлено!\n{self.print_balance()}\n")
#
#     def add_percent(self):
#         self.__balance += self.__balance * self.__percent
#         print(f"Проценты были успешно начислены!\n{self.print_balance()}\n")
#
#     def to_usd(self):
#         balance_usd = Account.converter(self.__balance, Account.__usd_course)
#         print(f"Состояние счёта: {balance_usd} {Account.__usd}")
#
#     def to_eur(self):
#         balance_eur = Account.converter(self.__balance, Account.__eur_course)
#         print(f"Состояние счета: {balance_eur} {Account.__eur}")
#
#     def print_balance(self):
#         return f"Текущий баланс {self.__balance} {Account.__rub}"
#
#     def account_info(self):
#         info = (f"Информация о счете:\n{"-" * 20}\n#{self.__number}\nВладелец: {self.__surname}\n"
#                 f"{self.print_balance()}\nПроценты: {self.__percent:.0%}\n")
#         print(info)
#
#
# person1 = Account("Долгих", "12345", 0.03, 1000)
# person1.account_info()
# person1.to_usd()
# person1.to_eur()
# Account.change_usd(2)
# Account.change_eur(3)
# print()
# person1.to_usd()
# person1.to_eur()
# person1.surname = "Дюма"
# person1.account_info()
# person1.add_percent()
# person1.withdrawal(100)
# person1.withdrawal(3000)
# person1.add_money(5000)
# person1.withdrawal(3000)

# Вариант №2
import re


class Account:
    __slots__ = ["__surname", "__number", "__percent", "__balance"]
    __usd_course = 0.012
    __eur_course = 0.011
    __rub = "RUB"
    __usd = "USD"
    __eur = "EUR"

    def __init__(self, surname, number, percent, balance):
        self.check_surname(surname)
        self.check_number(number)
        self.check_percent(percent)
        self.check_money(balance)
        self.__surname = surname
        self.__number = number
        self.__percent = percent
        self.__balance = balance
        print(f"Счёт #{self.__number} принадлежащий {self.__surname} был открыт.\n{"*" * 50}\n")

    def __del__(self):
        print(f"Счёт #{self.__number} принадлежащий {self.__surname} закрыт.\n{"*" * 50}")

    @classmethod
    def change_usd(cls, new_usd):
        Account.check_money(new_usd)
        cls.__usd_course = new_usd

    @classmethod
    def change_eur(cls, new_eur):
        Account.check_money(new_eur)
        cls.__eur_course = new_eur

    @staticmethod
    def converter(balance, exchange_rate):
        return balance * exchange_rate

    @staticmethod
    def check_surname(surname):
        if not isinstance(surname, str):
            raise TypeError("Некорректный тип данных при вводе фамилии")
        if not re.fullmatch(r"^[a-zа-яё-]+$", surname, re.IGNORECASE):
            raise ValueError("Некорректный ввод фамилии")

    @staticmethod
    def check_number(number):
        if not isinstance(number, (str, int)):
            raise TypeError("Некорректный тип данных для номера счёта")
        if not re.fullmatch(r"^1\d{4,15}$", str(number)):
            raise ValueError("Некорректный номер счёта")

    @staticmethod
    def check_percent(value):
        if not isinstance(value, float):
            raise TypeError("Некорректный тип данных для значения процента")
        if value < 0 or value > 1:
            raise ValueError("Некорректное значение величины процента")

    @staticmethod
    def check_money(money):
        if not isinstance(money, (int, float)):
            raise TypeError("Некорректный тип данных для произведения операции")
        if money <= 0:
            raise ValueError("Некорректное значение для произведения операции")

    def __get_surname(self):
        return self.__surname

    def __set_surname(self, new_surname):
        self.check_surname(new_surname)
        self.__surname = new_surname

    surname = property(__get_surname, __set_surname)

    def withdrawal(self, money):
        self.check_money(money)
        if money > self.__balance:
            print(f"К сожалению у вас нет {money} {Account.__rub} на счёте.\n{self.print_balance()}\n")
        else:
            self.__balance -= money
            print(f"Было успешно снято {money} {Account.__rub}\n{self.print_balance()}\n")

    def add_money(self, money):
        self.check_money(money)
        self.__balance += money
        print(f"{money} {Account.__rub} было успешно добавлено!\n{self.print_balance()}\n")

    def add_percent(self):
        self.__balance += self.__balance * self.__percent
        print(f"Проценты были успешно начислены!\n{self.print_balance()}\n")

    def to_usd(self):
        balance_usd = Account.converter(self.__balance, Account.__usd_course)
        print(f"Состояние счёта: {balance_usd} {Account.__usd}")

    def to_eur(self):
        balance_eur = Account.converter(self.__balance, Account.__eur_course)
        print(f"Состояние счета: {balance_eur} {Account.__eur}")

    def print_balance(self):
        return f"Текущий баланс {self.__balance} {Account.__rub}"

    def account_info(self):
        info = (f"Информация о счете:\n{"-" * 20}\n#{self.__number}\nВладелец: {self.__surname}\n"
                f"{self.print_balance()}\nПроценты: {self.__percent:.0%}\n")
        print(info)


person1 = Account("Долгих", "12345", 0.03, 1000)
person1.account_info()
person1.to_usd()
person1.to_eur()
Account.change_usd(2)
Account.change_eur(3)
print()
person1.to_usd()
person1.to_eur()
person1.surname = "Дюма"
person1.account_info()
person1.add_percent()
person1.withdrawal(100)
person1.withdrawal(3000)
person1.add_money(5000)
person1.withdrawal(3000)
