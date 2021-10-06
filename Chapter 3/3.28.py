num = input("정수를 입력하시오 : ")
num_List = list(map(int, str(num)))
output = True
for i in range(0, len(num_List) // 2):
    if not (num_List[i] == num_List[len(num_List) - i - 1]):
        output = False
        break

if output:
    print(num, "은(는) 거꾸로 정수입니다.")

else:
    print(num, "은(는) 거꾸로 정수가 아닙니다.")
