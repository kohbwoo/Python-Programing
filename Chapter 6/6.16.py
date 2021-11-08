student_tuple = (("191101", "홍길동", "010-123-45xx"), ("191102", "임꺽정", "010-223-45xx"), ("191103", "장길산", "010-323-45xx"))
student_dict = {num: name for num, name, tel in student_tuple}

print("학생정보:", student_dict)

while True:
    tmp = input("학번을 입력하세요 :")
    if tmp == "-1": break
    print(tmp, "번 학생은", student_dict[tmp], "입니다.")

print("프로그램을 종료합니다.")
