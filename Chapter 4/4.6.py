def cel2fah(cel):
    return (9/5)*cel+32


for i in range(10, 50+1, 10):
    print("섭씨", i, "도 = 화씨", cel2fah(i), "도")
