maxNum = None
minNum = None
while True:
    line = input('> ')
    if line == 'done':
        break
    try:
        number = float(line)
    except:
        print('Invalid Number')
        continue
    if minNum is None or number < minNum:
        minNum = number
    elif maxNum is None or number > maxNum:
        maxNum = number
       
print('Highest Number: ', maxNum)
print('Lowest Number: ', minNum)
