
import pandas as pd

def fuzzy_cartesian_product(A, B):
    R = {}  
    for x, mu_x in A.items():
        for y, mu_y in B.items():
            R[(x, y)] = min(mu_x, mu_y)
    return R

if __name__ == "__main__":
    A = {"x1": 0.2, "x2": 0.7}
    B = {"y1": 0.5, "y2": 0.4, "y3": 1.0}

    R = fuzzy_cartesian_product(A, B)

    print("Fuzzy Set A:", A)
    print("Fuzzy Set B:", B)

    print("\nFuzzy Relation (A x B) as pairs:")
    for pair, val in R.items():
        print(f"{pair}: {val}")

    print("\nFuzzy Relation (Matrix form):")
    matrix = pd.DataFrame(
        [[R[(x, y)] for y in B] for x in A],
        index=A.keys(),
        columns=B.keys()
    )
    print(matrix)
