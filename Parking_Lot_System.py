import datetime

Time = datetime.datetime.now()
# 차량번호     #입차시간
Car_List = [["14무5673", datetime.datetime(2021, 11, 15, 5, 15)],
            ["14무5674", datetime.datetime(2021, 11, 15, 5, 15)]]

clearConsole = lambda: print('\n' * 50)
Price_Of_10Min = 500
def Print_menus():
    print("\t주차장 요금 정산기")
    print("1.\t차량 입차")
    print("2.\t차량 출차")
    print("3.\t차량 조회")
    print("4.\t관리자 메뉴")


def Car_Entrance():
    print("차량 입차")
    New_Car_Num = input("차량번호를 입력하시면 현재시간으로 입차됩니다.")
    Car_List.append([New_Car_Num, datetime.datetime.now()])


def Car_Inquire():
    clearConsole()
    print("차량 조회")
    print("차량번호 \t\t 입차날짜\t\t입차시간\t  할인\t주차비용")
    for i in Car_List:
        print(str(i[0]) + "\t", i[1].strftime("%Y-%m-%d %H:%M:%S"))
    input("초기화면으로 돌아가려면 아무키나 입력하세요")
    clearConsole()

def Car_Out():
    print("차량 출차")
    Car_Num = input("출차 할 차량의 번호를 입력해주세요")
    key = 0
    for i in range(0, len(Car_List)):
        if i == Car_Num:
            key = i

    print(Car_List[key][0], "차량의 경과 시간은", (Car_List[key][1] - datetime.datetime.now()) , "\n요금은 -- 원 입니다.")
    print(Car_List[key][0], "차량의 경과 시간은", (Car_List[key][1] - datetime.datetime.now()).seconds,"\n요금은 -- 원 입니다.")

def Admin_Setting():
    print("관리자 메뉴")
    Price_Of_10Min = int(input("변경하실 10분당 주차 요금을 입력하세요."))

while True:
    Print_menus()
    User_Input = input("번호를 입력하세요.\n")

    if User_Input == "1":
        Car_Entrance()

    elif User_Input == "2":
        Car_Out()

    elif User_Input == "3":
        Car_Inquire()

    elif User_Input == "4":
        Admin_Setting()

    else:
        clearConsole()
        print("잘못 입력하셨습니다. 초기화면으로 돌아갑니다.")
