class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass


Dog1 = Dog()
Dog1.walk()
