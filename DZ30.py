import json
from random import choice


def gen_person():
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'k', 'l', 'm', 'n']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)
    # print(name)

    while len(tel) != 10:
        tel += choice(nums)

    person = {
        'name': name,
        'tel': tel
    }
    return person, tel


def write_json(person_dict, num):
    try:
        data = json.load(open("persons_dict.json"))
    except FileNotFoundError:
        data = {}
    data[num] = person_dict
    with open("persons_dict.json", "w") as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person()[0], gen_person()[1])
