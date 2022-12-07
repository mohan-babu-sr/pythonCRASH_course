class FirstClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def move():
        print('move')

    @staticmethod
    def draw():
        print('draw')

    def talk(self):
        print(f'Talking to {self.x}')


class1 = FirstClass("mohan", 20)
class1.draw()
class1.talk()
print(class1.x)
