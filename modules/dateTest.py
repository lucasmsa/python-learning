import datetime

d = datetime.date(2020, 2, 2)
print(d)

today = datetime.date.today()
print(today)    
print(today.year)
print(today.weekday())

tDelta = datetime.timedelta(days=7)
print(tDelta)

christmas = datetime.date(2020, 12, 25)
tillChristmas = christmas - today
print(tillChristmas)