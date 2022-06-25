"""
Dates
"""

import datetime

today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
print(today.isoweekday())

create_day = datetime.date(2022, 6, 25)
print(create_day)

next_year = datetime.date(2023, 1, 1)

days_remaining = next_year - create_day
print(days_remaining)
print(days_remaining.days)