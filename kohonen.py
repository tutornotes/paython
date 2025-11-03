
import numpy as np

# Input patterns (4 features)
data = np.array([
    [0, 0, 1, 1],
    [1, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 1]
])

# Initial weights (features x neurons)
weights = np.array([
    [0.2, 0.9],
    [0.4, 0.7],
    [0.6, 0.5],
    [0.8, 0.3]
])

# Learning rate
alpha = 0.5

# Training without epochs (just one pass over all inputs)
print("KSOFM Training :")
for idx, x in enumerate(data, start=1):
    # Calculate squared Euclidean distance to each neuron
    dists = np.sum((weights - x[:, np.newaxis]) ** 2, axis=0)
    winner = np.argmin(dists)
    print(f"  Input x[{idx}] = {x}, distances = {np.round(dists, 4)}, winner = Neuron {winner + 1}")

    # Update weights of winning neuron
    for i in range(len(x)):
        weights[i][winner] += alpha * (x[i] - weights[i][winner])
    # Print updated weights cleanly
    formatted_weights = [f"{weights[i][winner]:.4f}" for i in range(len(x))]
    print(f"  Updated weights for Neuron {winner + 1}: {formatted_weights}")

# Final weights display
print("\nFinal Weights After One Pass:")
for i in range(weights.shape[0]):
    row = [f"{val:.4f}" for val in weights[i]]
    print(f"  {row}")