from datetime import date,time,datetime,timedelta

today = date.today()

print(today)
print(today.year)
print(today.month)
print(today.day())
print(today.weekday()) # 0-6
print(today.isoweekend()) # 1-7

d = date(2025-9-31)
print(d) # error - date is out of range for the month

d = date(2025-2-28) # this is for when we enter the date of birth in forms to check entered the valid date or not
t = time(23,59,12) # to check the entered time id valid or not
specific_datetime = datetime(2024, 2, 16, 14, 30, 15) # when we need date and tme together 

now=datetime.now
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)

