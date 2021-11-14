import datetime
Start_day = datetime.datetime.strptime('2019/02/24','%Y/%m/%d')
To_day = datetime.datetime.today()

print("춘향이와 몽룡이의 연애 시작일 :", Start_day.year,"년",Start_day.month,"월", Start_day.day,"일")
print("연애 시작일로부터 경과한 날짜", abs((Start_day - To_day).days),"일")
After_100day = (Start_day + datetime.timedelta(days=100))
After_200day = (Start_day + datetime.timedelta(days=200))
After_500day = (Start_day + datetime.timedelta(days=500))
After_1000day = (Start_day + datetime.timedelta(days=1000))
print("100일 기념일 :", After_100day.year,"년", After_100day.month,"월", After_100day.day,"일")
print("100일 기념일 :", After_200day.year,"년", After_200day.month,"월", After_200day.day,"일")
print("100일 기념일 :", After_500day.year,"년", After_500day.month,"월", After_500day.day,"일")
print("100일 기념일 :", After_1000day.year,"년", After_1000day.month,"월", After_1000day.day,"일")