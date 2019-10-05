x = 50


def func():
    global x

    print('x равно', x)
    x = 2
    print('Change global value x on', x)


func()
print('Value x is:', x)





