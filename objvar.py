class Robot:
    """
    представляет робота с именем.
    """
    # переменная класса, содержащая количество роботов
    population = 0

    def __init__(self, name):
        """
        Инициализация данных.
        """
        self.name = name
        print('(Инициализация {0})'.format(self.name))
        # При создании этой личности, робот добавляется
        # к переменной 'population'
        Robot.population += 1

    def __del__(self):
        """
        Я умираю.
        """
        print('{0} уничтожается!'.format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print('{0} был последним.'.format(self.name))
        else:
            print('Осталось {0} работающих роботов.'.format(Robot.population))

    def say_hi(self):
        """
        Приветствие робота.
        Да, они это могут.
        """
        print('Приветствую! Мои хозяева называют меня {0}.'.format(self.name))

    @staticmethod
    def how_many():
        """
        Выводит численность роботов.
        """
        print('У нас {0} роботов.'.format(Robot.population))


droid1 = Robot('R2-D2')

droid1.say_hi()
droid1.how_many()

Robot.how_many()







