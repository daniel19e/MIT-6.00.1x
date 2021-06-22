# this function returns the remaining debt after one year of payments with interest
def debt(balance, annualInterestRate, monthlyPaymentRate):
    month = 0
    while month < 12:
        balance -= monthlyPaymentRate*balance
        balance = balance + annualInterestRate/12 * balance
        month += 1
    return round(balance, 2)
