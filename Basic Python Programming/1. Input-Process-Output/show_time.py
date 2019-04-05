import datetime

time = datetime.datetime.now()
print(time)

date = datetime.date.today()
print("Today's Date =", date)
print("Current year =", date.year)
print("Current month =", date.month)
print("Current day =", date.day)

t = datetime.timedelta(days = 5, hours = 1, seconds = 33, microseconds = 224333)
print("total_seconds =", t.total_seconds())

british_date = time.strftime("%d %m %Y")
american_date = time.strftime("%m %d %Y")

print("British Date Format =", british_date)
print("American Date Format =", american_date)