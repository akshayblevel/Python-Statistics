list = []

print("Enter the numbers ::")
num = 0
i = 0

while i < 10:
    num = int(input("Enter number -->"))
    list.append(num)
    i = i + 1

list.sort()

median = 0
center = len(list)//2

if(len(list)%2 == 1):
    median = list[center]
else:
    median = (list[center]+list[center-1])/ 2

print("The median is ",median)