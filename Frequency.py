# Finding number frequency

list = [14,10,81,17,10,17,16,11,84]

num = int(input("Enter number  "))

count = 0

for v in list:
    if(v == num ): count = count + 1

print("The frequency of number is ",count)