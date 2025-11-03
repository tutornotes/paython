
import numpy as np

e1 = np.array([1, -1, -1, -1])
e2 = np.array([-1, -1, -1, 1])

w = 0.5 * np.array([e1, e2]).T
print("Weight matrix (w):\n", w)

bias = np.array([2, 2])

x = np.array([
    [-1, -1, 1, -1],
    [-1, -1, 1, 1],
    [-1, -1, -1, 1],
    [1, 1, -1, -1]
])

def hamming_net_output(x, w, bias):
    y_in = bias + np.dot(x, w)
    return y_in

def maxnet(y, epsilon=0.1, max_iter=10):
    y = np.copy(y)
    for _ in range(max_iter):
        new_y = np.copy(y)
        for i in range(len(y)):
            inhibition = epsilon * sum(y[j] for j in range(len(y)) if j != i)
            new_y[i] = max(0, y[i] - inhibition)
        if np.allclose(new_y, y):
            break
        y = new_y
    return y

print("\n--- Hamming Net and Maxnet Output ---")
for i, input_x in enumerate(x):
    print(f"\nInput x{i+1} = {input_x}")
    y_raw = hamming_net_output(input_x, w, bias)
    print(f"Initial Output (y_in) = {y_raw}")
    y_final = maxnet(y_raw)
    print(f"Maxnet Final Output = {y_final}")
    winner_indices = np.where(y_final == np.max(y_final))[0]
    if len(winner_indices) == 1:
        print(f"Assigned to cluster: e{winner_indices[0]+1}")
    else:
        winner_clusters = [f"e{idx+1}" for idx in winner_indices]
        print(f"Ambiguous Match: Possibly {' and '.join(winner_clusters)}")