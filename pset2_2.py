balance = 5000
annualInterestRate = 0.2
monthlyPayment = 10
temp = balance
epsilon = 0.01
while temp > 0:
    for month in range(12):
        temp = temp-monthlyPayment + \
            annualInterestRate/12 * (temp-monthlyPayment)
    if temp <= 0:
        print(round(monthlyPayment, 2))
        break
    else:
        monthlyPayment += 10
        temp = balance
