import datetime
Start_day = datetime.datetime.strptime('2019/02/24','%Y/%m/%d')
To_day = datetime.datetime.today()

print("춘향이와 몽룡이의 연애 시작일 :", Start_day.year,"년",Start_day.month,"월", Start_day.day,"일")
print("연애 시작일로부터 경과한 날짜", abs((Start_day - To_day).days),"일")
