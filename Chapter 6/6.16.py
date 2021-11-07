student_tuple = (("191101", "홍길동", "010-123-45xx"), ("191102", "임꺽정", "010-223-45xx"), ("191103", "장길산", "010-323-45xx"))

tmp = [n for n,x in enumerate(student_tuple) if x=='191101']
print(tmp)


# while True:
#     tmp = input("학번을 입력하세요 :")
#     print(tmp,"번 학생은", student_tuple)
