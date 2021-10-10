menu = ["햄버거", "치킨", "피자"]
print("맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
print("1) 햄버거 (입력 b)")
print("2) 치킨(입력 c)")
print("3) 피자(입력 p)")
choice = input("1에서 3까지의 메뉴를 선택하세요 :")
while True:
    if choice == "b":
        print("햄버거를 선택하였습니다.")
        break

    elif choice == "c":
        print("치킨을 선택하였습니다.")
        break

    elif choice == "p":
        print("피자를 선택하였습니다.")
        break
    else:
        choice = input("메뉴를 다시 입력하세요(알파벳 b, c, p 입력) :")
        continue
