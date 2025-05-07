# data_analysis.py

import pandas as pd
import numpy as np

# Generate random data
np.random.seed(0)
data = np.random.randint(1, 101, 50)  # 50 random integers between 1 and 100

# Convert to DataFrame
df = pd.DataFrame(data, columns=['Numbers'])

# Calculate statistics
mean_value = df['Numbers'].mean()
median_value = df['Numbers'].median()
std_dev = df['Numbers'].std()

# Display results
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Standard Deviation: {std_dev}")


