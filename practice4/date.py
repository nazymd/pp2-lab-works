from datetime import datetime, date, time, timedelta
today=date.today()
past=today-timedelta(days=5)
print (today)
print(past)

today=date.today()
yesterday=today-timedelta(days=1)
tommorrow=today+timedelta(days=1)
print (yesterday, today, tommorrow)


now = datetime.now()
drop = now.replace(microsecond=0)
print("with microseconds:", now)
print("without microseconds:", drop)


date1_str = input("YYYY-MM-DD HH:MM:SS: ")
date2_str = input("YYYY-MM-DD HH:MM:SS: ")
date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")
diff = date2 - date1
seconds = diff.total_seconds()
print(seconds)
