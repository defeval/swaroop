def printMax(x, y):
    """

    :param x: int
    :param y: int
    :return: max value
    """

    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'max')
    else:
        print(y, 'max')


printMax(3, 5)
print(printMax.__doc__)

