# Differential Privacy: Differential privacy adds a controlled amount of noise to the query results, ensuring that the results do not leak sensitive information about any individual data point. By introducing randomness, it becomes challenging to identify specific records, even if someone tries to analyze the aggregated results.

import numpy as np

# Original data
data = np.random.rand(100)

# Compute the sum in a differentially private manner
def dp_sum(data, epsilon):
    noise = np.random.laplace(0, 1/epsilon, 1)
    return np.sum(data) + noise

result = dp_sum(data, 0.1)

print(result)
