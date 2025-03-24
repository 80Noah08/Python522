def decor(fn):
    def wrap(*args):
        sr = sum(args) / len(args)
        print("Сумма чисел:", *args, "=", sum(args))
        print("Среднее арифметическое чисел:", *args, "=", sr)

    return wrap


@decor
def func(*args):
    return args


func(2, 3, 3, 4)
