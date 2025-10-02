list = []

num = 0
i = 0

while i < 10:
    num = int(input("Enter each number -->"))
    list.append(num)
    i = i + 1

sum = 0

for v in list:
    sum = sum + v

average = sum/len(list)

print("The average is ",average)