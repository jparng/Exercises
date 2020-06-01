count = 0
total = 0
average = 0
while True:
    line = input('> ')
    if line == 'done':
        break
    try:
        number = float(line)
    except:
        print('Invalid Number')
        continue
    count = count + 1
    total = total + number
    average = total / count
       
print('Count: ' , count)
print('Total: ', total)
print('Average: ', average)
