import random
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def addlist(num, arr):
    for i in range(num):
        arr.append(random.randint(1,100))
    return arr

arr = []
num = 10
arr = addlist(num, arr)


print(arr)
arr = selection_sort(arr)
print(arr)

