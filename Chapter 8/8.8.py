import random#8.8

Random_List = ""

for i in range(0,10):
    Random_List = Random_List + (str(random.randint(1,1000))) + " "

f = open('random_numbers.txt', 'w')
f.write(str(Random_List))
f.close()
