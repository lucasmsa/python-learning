import datetime
import calendar


# starting balance, and each month 400 money units will be paid
# and the interest rate will be multiplied by the current balance
# Ex.: how long will it take to pay off credit card balance
balance = 2000
interestRate = 14 * .01
print(interestRate)
monthlyPayment = 400

# Gets today's day, afterwards, checks the
# first day of the next month
today = datetime.date.today()

monthTuple = calendar.monthrange(today.year, today.month)

# This will return a tuple containing two values
# the first one is the first day of the month 
# second is the number of days in the month
print(monthTuple)

daysInCurrentMonth = monthTuple[1]
# Gets how many days until the month end
daysTillMonthEnd = daysInCurrentMonth - today.day
print(daysTillMonthEnd)

dateStart = today + datetime.timedelta(days=daysTillMonthEnd + 1)
dateEnd = dateStart

while balance > 0:
    interestCharge = (interestRate / 12) * balance
    balance += interestCharge
    balance -= monthlyPayment

    # one-liner if/else
    # Round balance to 2 decimal places
    balance = 0 if balance < 0 else round(balance, 2)

    print(dateEnd,  balance)

    monthTuple = calendar.monthrange(dateEnd.year, dateEnd.month)
    dateEnd = dateEnd + datetime.timedelta(days=daysInCurrentMonth)

    

