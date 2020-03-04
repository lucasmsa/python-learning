import datetime

# weightloss script
currentWeight = 73
goalWeight = 67
avgKgPerWeek = 0.45

startDate = datetime.date.today()
endDate = startDate

while currentWeight > goalWeight:

    # adding 7 days to simulate a week passing
    endDate += datetime.timedelta(days=7)
    currentWeight -= avgKgPerWeek
    
    print(endDate, round(currentWeight, 2))


print(f"Start date: {startDate.month.no}, end date: {endDate}    ")
print(f"Weeks to achieve weight goal: {(endDate - startDate).days // 7}, {(endDate - startDate).days} days")