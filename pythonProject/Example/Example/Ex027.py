import datetime

print(datetime.datetime.now())
now_date = datetime.datetime.now()
print(now_date.year)
print(now_date.month)

format_date = now_date.strftime("%m/%d/%Y %H-%M-%S")
print(format_date)