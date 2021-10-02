menu = ["햄버거", "치킨", "피자"]
num = 0
print("맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
for i in range(3):
    print(str(i + 1) + ")", menu[i])
num = int(input("1에서 3까지의 메뉴를 선택하세요 :")) - 1
while True:
    if not (-1 < num < 3):
        num = int(input("메뉴를 다시 입력하세요:")) - 1
        continue
    else:
        print(str(menu[num]) + "을 선택하였습니다.")
        break
