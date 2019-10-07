class Person:
    def __init__(self, name):
        self.name = name

    def sayhi(self):
        print('Привет! Меня зовут', self.name)


p = Person('Swaroop')
p.sayhi()
