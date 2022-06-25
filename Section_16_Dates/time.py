"""
Time
"""

import datetime

time = datetime.time(1, 2, 44, 100)
print(time)

date_time = datetime.datetime(2022, 6, 25, 14, 26, 000)
print(date_time)

time_delta = datetime.timedelta(days=16)
print(date_time + time_delta)
time_delta = datetime.timedelta(minutes=45)
print(date_time + time_delta)

date_string = '2022-11-02'
date_object = date_time.date().fromisoformat(date_string)
time_delta = datetime.timedelta(days=16)
print(date_object + time_delta)