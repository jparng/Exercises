hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

def computepay(hours, rate):
    if hours > 40:
        overHours = float(hours - 40)
        overtime = float(overHours * (rate * 1.5)) #included statement to add overtime
        pay = float((hours - overHours) * rate)
        totalpay = pay + overtime
        return totalpay
    else:
        regpay = hours * rate
        return regpay
    

print(computepay(hours, rate))



