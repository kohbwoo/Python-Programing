menu = {"Americano": "3000", "Ice Americano": "3500", "Cappuccino": "4000", "Caffe Latte": "4000", "Espresso": "3600"}

for key in menu:
    if len(key) < 11:
        tmp = "\t\t"
    else:
        tmp = "\t"
    print(key, tmp, menu[key])

choice = input("위의 메뉴중 하나를 선택하세요: ")
print(choice, "는", menu[choice],"원 입니다. 결제를 부탁합니다.")