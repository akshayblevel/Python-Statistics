data = [14,10,81,17,10,17,16,11,84]


def mean(data):
   if len(data) == 0:
       raise ValueError("Cannot calculate mean of an empty list")
   return sum(data) / len(data)

print("Mean: ",mean(data))