import numpy as np
import matplotlib.pyplot as plt

# Parameters for the normal distribution
population_mean = 50
population_std = 15
sample_size = 5
num_samples = 1000

# Create empty list to store sample means
sample_means = []

# Sampling loop
for _ in range(num_samples):
   # Generate a random sample from the normal distribution
   sample = np.random.normal(population_mean, population_std, size=sample_size)

   # Calculate the mean of the sample
   sample_mean = np.mean(sample)

   # Store the sample mean
   sample_means.append(sample_mean)

# Plot the distribution of sample means
plt.hist(sample_means)
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.title("Distribution of Sample Means (Normal Population)")
plt.show()