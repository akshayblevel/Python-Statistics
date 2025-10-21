import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Parameters for the uniform distribution
lower_bound = 0.0
upper_bound = 10.0

# Generate a large sample of uniformly distributed data
data = np.random.uniform(lower_bound, upper_bound, size=100000)

# Visualize the distribution using Seaborn's histplot
sns.histplot(data, kde=True, stat='density')
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Uniform Distribution')
plt.show()