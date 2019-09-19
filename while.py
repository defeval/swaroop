number = 23
running = True

while running:
    guess = int(input('Enter a number: '))

    if guess == number:
        print('Well!')
        running = False  # Stop while
    elif guess < number:
        print('Guess > Number')
    else:
        print('Guess < Number')
else:
    print('While done')

print('DOne')
