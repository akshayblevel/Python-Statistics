data = [14, 10, 81, 16, 11, 84, 17, 10, 17]

def mean(data):
   if len(data) == 0:
       raise ValueError("Cannot calculate mean of an empty list")
   return sum(data) / len(data)

def variance(data):
   if len(data) == 0:
       raise ValueError("Cannot calculate variance of an empty list")
   avg = mean(data)
   print("average: ", avg )
   squared_deviations = [(x - avg) ** 2 for x in data]
   print("Squared Deviation: ", squared_deviations)
   return sum(squared_deviations) / len(data)

print("Variance: ",variance(data))

'''
average:  28.88888888888889
Squared Deviation:  [221.679012345679, 356.7901234567901, 2715.567901234568, 166.12345679012347, 320.01234567901236, 3037.234567901235, 141.3456790123457, 356.7901234567901, 141.3456790123457]
Variance:  828.5432098765433
'''