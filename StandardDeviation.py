import math

data = [14, 10, 81, 16, 11, 84, 17, 10, 17]


def mean(data):
   if len(data) == 0:
       raise ValueError("Cannot calculate mean of an empty list")
   return sum(data) / len(data)

def variance(data):
   if len(data) == 0:
       raise ValueError("Cannot calculate variance of an empty list")
   avg = mean(data)
   squared_deviations = [(x - avg) ** 2 for x in data]
   return sum(squared_deviations) / len(data)


def std_deviation(data):
   return math.sqrt(variance(data))

print("Standard Deviation: ",std_deviation(data))

'''
Standard Deviation:  28.78442651637415
'''