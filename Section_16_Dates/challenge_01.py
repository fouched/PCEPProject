
import datetime

date_today = datetime.date.today()
print(date_today)

birthday = datetime.date(2022, 11, 2)
days_remaining = birthday - date_today
print(days_remaining.days)

time_delta = datetime.timedelta(days=20)
twenty_days = date_today + time_delta
print(twenty_days)
print(twenty_days.isoweekday())

today_string = '2020-12-04'
today_date = datetime.date.fromisoformat(today_string)
print(today_date)
