name = input("What's your name? ") # Asks for a name and prints it out
print('Hello ' + name + '!')

hours = float(input('Enter your hours: '))  # Asks for number of hours at 
rate = float(input('Now enter your rate: ')) #rate and then calculates the pay
pay = int(hours * rate)
print('Here is your pay: ' + str(pay))

fah = float(input("What's the temperature outside(in Celius)? "))
ctof = (fah * (9/5)) + 32
print("It's " + str(ctof) + ' degrees outside in fahrenheit')
