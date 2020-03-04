import datetime
import math

# Get to a certain goal of subscribers
goalSubs = 1000
currentSubs = 700
subsToGo = goalSubs - currentSubs

avgSubsDay = 15
daysToGo = round(subsToGo / avgSubsDay) 

today = datetime.date.today()   
print(today)
print(today + datetime.timedelta(days=daysToGo))