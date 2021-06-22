balance = 5000
annualInterestRate = 0.2

temp = balance  # temporal variable to hold and reset balance value
monthlyInterestRate = annualInterestRate/12
lowerBound = balance/12
upperBound = (balance*(1+monthlyInterestRate)**12)/12.0
epsilon = 0.01
while abs(temp) > epsilon:
    # find the middle of the bounds to find an approximate answer
    guess = (upperBound+lowerBound)/2
    temp = balance  # reset the value of the balance every time the loop runs
    for month in range(12):  # calculate the total balance after 12 months and interest
        unpaid = temp-guess
        temp = unpaid + (monthlyInterestRate * (unpaid))
    if temp > epsilon:  # if guess is too high, change the lower bound to be our guess
        lowerBound = guess
    elif temp < epsilon:  # if guess is too low, change upper bound to be our guess
        upperBound = guess
print(round(guess, 2))
