
inputs = [
    [-1, -1, -1],
    [-1, 1, 1],
    [1, -1, 1],
    [1, 1, 1]
]
targets = [-1, -1, -1, 1]
weights = [0, 0, 0]

print("Training using Hebbian Learning Rule:\n")

for i in range(4):
    x = inputs[i]
    t = targets[i]
    print(f"Input {i+1}: {x}, Target: {t}")
    for j in range(3):
        weights[j] += x[j] * t
    print(f"Updated Weights: {weights}\n")

print("Final Weights:", weights)

print("\nTesting the network with final weights:")
for x in inputs:
    y = sum(i * w for i, w in zip(x, weights))
    print(f"Input: {x[:-1]}, Bias: {x[2]}, Output: {y}")




