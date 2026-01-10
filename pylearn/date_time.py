import datetime
date = datetime.date(2026,1,10)
today = datetime.date.today()



time = datetime.time(12,30,45)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %m-%d-%y")

target = datetime.datetime(2026,2,2,12,23,1)
current_datetime = datetime.datetime.now()


if target < current_datetime:
    print("This date and time already passed")
else:
    print("Target date has not passed")
