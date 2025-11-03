
import numpy as np
import pandas as pd

def max_min_composition(R1, R2):
    R1 = np.array(R1)
    R2 = np.array(R2)

    if R1.shape[1] != R2.shape[0]:
        raise ValueError("Incompatible relations: columns of R1 must be equal to rows of R2")

    result = np.zeros((R1.shape[0], R2.shape[1]))

    for i in range(R1.shape[0]):
        for j in range(R2.shape[1]):
            for k in range(R1.shape[1]):
                result[i, j] = max(result[i, j], min(R1[i, k], R2[k, j]))

    return result

if __name__ == "__main__":
    R1 = [
        [0.2, 0.7, 1.0],
        [0.5, 0.4, 0.6]
    ]

    R2 = [
        [0.6, 0.2],
        [0.8, 0.5],
        [0.3, 0.9]
    ]

    R = max_min_composition(R1, R2)

    print("Relation R1 (X-Y):")
    print(pd.DataFrame(R1))

    print("\nRelation R2 (Y-Z):")
    print(pd.DataFrame(R2))

    print("\nMax-Min Composition (R1 o R2) (X-Z):")
    print(pd.DataFrame(R))
