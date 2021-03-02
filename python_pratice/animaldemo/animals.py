import yaml


class Animal():
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def run(self, iscall):
        print(f'叫声是：{iscall}')
        print('会跑')


class Cat(Animal):
    def __init__(self, hair, name, color, age, gender):
        self.hair = hair
        super().__init__(name, color, age, gender)

    def cat_skill(self):
        print('抓老鼠')


class Dog(Animal):
    def __init__(self):
        self.hair = '长毛'
        super().__init__()

    def dog_skill(self):
        print('会看家')


if __name__ == '__main__':
    with open("animal-type.yml") as f:
        datas = yaml.safe_load(f)
    eb = datas['default']['name']
    print(eb)
