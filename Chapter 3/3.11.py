key = [2, 3, 9]  # 당첨번호
num = [0, 0, 0]  # 입력받을 번호 리스트

num[0], num[1], num[2] = input('세 복권번호를 입력하시오 : ').split()
num[0], num[1], num[2] = int(num[0]), int(num[1]), int(num[2])  # int 형으로 변경 변경

point = 0  # 맞은 갯수를 카운트할 변수

for i in range(0, 3):
    for j in range(0, 3):
        if num[i] == key[j]:
            point = point + 1  # 당첨번호와 입력번호가 같은경우 포인트 1점 추가

if point == 0:  # 포인트에 따라 상금 출력
    print("다음 기회에...")
elif point == 1:
    print("상금 1만 원")
elif point == 2:
    print("상금 1천만 원")
elif point == 3:
    print("상금 1억 원")
