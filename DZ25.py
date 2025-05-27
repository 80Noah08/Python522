class Student:
    def __init__(self, name, model="HP", cpu="i7", ram=16):
        self.name = name
        self.notebook = self.Notebook(model, cpu, ram)
        print(f"{self.name} => {self.notebook}")

    class Notebook:
        def __init__(self, model, cpu, ram):
            self.model = model
            self.cpu = cpu
            self.ram = ram

        def __str__(self):
            return f"{self.model}, {self.cpu}, {self.ram}"


st1 = Student("Roman")
st2 = Student("Vladimir")
