# import datetime
# date = datetime.datetime.now()
# print("현재 시간은", str(date.year) + "년", str(date.month) + "월", str(date.day) + "일입니다.")
# print("지금 태어난 아이의 주민등록번호 앞자리는 :", (date.year % 100 * 10000) + (date.month * 100) + date.day)
import datetime
Date = datetime.datetime.now()
Year, Month, Day = Date.year, Date.month, Date.day
print("현재 시간은 {}년 {}월 {}일 입니다. ".format(Year, Month, Day))


print("지금 태어난 아이의 주민등록번호 앞자리는 : ", str(Year)[2:] + str(Month) + str(Day))

