num = []
print("세 수를 입력하세요 :")
for i in range(3): num.append(int(input()))
num.sort()
print("정렬된 리스트는 다음과 같습니다:", num[0], num[1], num[2])