mylist = [(1, 2), (4, 5), (4, 2), (3, 1), (9, 4)]

a = input("두 정수를 입력하세요.").split()
a = tuple(map(int, a))
print(a)
for i in mylist:
    if a == i:
        print(mylist.index(a),"번째에", a,"요소가 있습니다.")
        break
    if (a[1], a[0]) == i:
        print(a,"요소는 없지만" ,mylist.index(a[1], a[0]), "번째에", (a[1],a[0]), "요소가 있습니다.")
        break

    if i == mylist[-1]:
        print("해당 요소가 없습니다.")
