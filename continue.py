while True:
    s = input('Input anything: ')
    if s == 'escape':
        break
    if len(s) < 3:
        print('Too short')
        continue
    print('String is good')
