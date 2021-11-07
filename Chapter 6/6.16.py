student_tuple = (("191101", "홍길동", "010-123-45xx"), ("191102", "임꺽정", "010-223-45xx"), ("191103", "장길산", "010-323-45xx"))
while True:
    tmp = input("학번을 입력하세요 :")
    if tmp == "-1": break
    for i in student_tuple:
        if i[0] == tmp:
            ans = i[1]
    print(tmp, "번 학생은", ans, "입니다.")
print("프로그램을 종료합니다.")
