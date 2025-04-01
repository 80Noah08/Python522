class Car:
    def __init__(self, model, year, manufacturer, power, colour, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.power = power
        self.colour = colour
        self.price = price
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.model}\nГод выпуска: {self.year}\nПроизводитель: {self.manufacturer}"
              f"\nМощность двигателя: {self.power}\nЦвет машины: {self.colour}\nЦена: {self.price}")
        print("=" * 40)

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_manufacturer(self):
        return self.manufacturer

    def set_power(self, power):
        self.power = power

    def get_power(self):
        return self.power

    def set_colour(self, colour):
        self.colour = colour

    def get_colour(self):
        return self.colour

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


c1 = Car("X7 M50i", "2021", "BMW", "530 л.с.", "white", "10.790.000")

c1.set_model("Tuatara")
print(c1.get_model())

c1.set_year("2020")
print(c1.get_year())

c1.set_manufacturer("SSC")
print(c1.get_manufacturer())

c1.set_power("1350 л.с.")
print(c1.get_power())

c1.set_colour("Графит")
print(c1.get_colour())

c1.set_price("142.500.000")
print(c1.get_price())
