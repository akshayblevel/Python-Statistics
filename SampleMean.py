import numpy as np
import matplotlib.pyplot as plt

# Parameters
population_min = 0
population_max = 100
sample_size = 5
num_samples = 1000

# Create empty list to store sample means
sample_means = []

# Sampling loop
for _ in range(num_samples):
   # Generate a random sample
   sample = np.random.randint(
       population_min, population_max + 1, size=sample_size)

   # Calculate the mean of the sample
   sample_mean = np.mean(sample)

   # Store the sample mean
   sample_means.append(sample_mean)

# Plot the distribution of sample means
plt.hist(sample_means)
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.title("Distribution of Sample Means (Uniform Population)")
plt.show()