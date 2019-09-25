x = 50


def func(x):
    print('x = ', x)
    x = 2
    print('Change local x on', x)


func(x)
print('x totaly ', x)

