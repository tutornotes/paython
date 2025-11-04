
import numpy as np

def bipolar_sign(x):
    return np.where(x >= 0, 1, -1)


X = np.array([
    [1, 1, 1, 1, -1, -1, 1, 1, 1, -1, 1, -1, 1, 1, 1],  
    [1, 1, 1, 1, -1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]   
])

Y = np.array([
    [-1, 1],  
    [1, 1]    
])


W = X.T @ Y
print("Weight matrix W:\n", W)


def recall_bam(x_input, W, max_iters=10):
    x = x_input.copy()
   
    for _ in range(max_iters):
        y = bipolar_sign(x @ W)
        x_new = bipolar_sign(y @ W.T)
        if np.array_equal(x_new, x):
            break
        x = x_new
    return x, y


for idx, x in enumerate(X):
    x_out, y_out = recall_bam(x, W)
    print(f"\nInput Pattern {chr(69 + idx)}: {x}")
    print(f"Recalled Output Y: {y_out}")