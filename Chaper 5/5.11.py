numlist = list(map(int, input("5개의 수를 입력 하세요: ").split()))

print("합 :", sum(numlist))
print("평균 :", sum(numlist)/len(numlist))
print("최댓값 :", max(numlist))
print("최솟값 :", min(numlist))
