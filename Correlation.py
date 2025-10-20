import math

X = [1, 2, 3, 4, 5 ]
Y = [10, 20, 30, 40, 50]

mean_X = sum(X)/len(X)
mean_Y = sum(Y)/len(Y)
print("Mean_X",mean_X)  # Mean_X 3.0
print("Mean_Y",mean_Y)  # Mean_Y 30.0

deviations_X = [x - mean_X for x in X]
deviations_Y = [y - mean_Y for y in Y]

print("Deviation X ",deviations_X)  # Deviation X  [-2.0, -1.0, 0.0, 1.0, 2.0]
print("Deviations Y ",deviations_Y) # Deviations Y  [-20.0, -10.0, 0.0, 10.0, 20.0]

squared_deviation_X = [x ** 2 for x in deviations_X]
squared_deviation_Y = [y ** 2 for y in deviations_Y]

print("Squared Deviation X ",squared_deviation_X)   # Squared Deviation X  [4.0, 1.0, 0.0, 1.0, 4.0]
print("Squared Deviation Y ",squared_deviation_Y)   # Squared Deviation Y  [400.0, 100.0, 0.0, 100.0, 400.0]

variance_X = sum(squared_deviation_X) / len(X)
variance_Y = sum(squared_deviation_Y) / len(Y)

print("Variance X ",variance_X) # Variance X  2.0
print("Variance Y ",variance_Y) # Variance Y  200.0

products = [a * b for a, b in zip(deviations_X, deviations_Y)]
covariance = sum(products) / len(X)

print("Covariance ",covariance) # Covariance  20.0

std_X = math.sqrt(variance_X)
std_Y = math.sqrt(variance_Y)
print("Standard deviation X ",std_X)    # Standard deviation X  1.4142135623730951
print("Standard deviation Y:",std_Y)    # Standard deviation Y: 14.142135623730951

correlation = covariance / (std_X * std_Y)
print("Correlation:", correlation)  # Correlation: 0.9999999999999998