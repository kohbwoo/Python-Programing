import datetime as dt
d = dt.date(2000, 12, 15) \
    - dt.timedelta(weeks = 2, days = 1)#2주 1일전
print(d.month)#11
print(d.day)#30
print(d.month + d.day)#41