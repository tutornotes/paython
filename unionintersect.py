
def fuzzy_union(A, B):
    """Union of fuzzy set A and B"""
    return {x: max(A.get(x, 0), B.get(x, 0)) for x in set(A) | set(B)}

def fuzzy_intersection(A, B):
    """Intersection of fuzzy set A and B"""
    return {x: min(A.get(x, 0), B.get(x, 0)) for x in set(A) | set(B)}

def fuzzy_complement(A):
    """Complement of fuzzy set A"""
    return {x: 1 - A[x] for x in A}

def fuzzy_difference(A, B):
    """Difference of fuzzy set A and B (A - B = A ∩ B')"""
    B_comp = fuzzy_complement(B)
    return fuzzy_intersection(A, B_comp)

if __name__ == "__main__":
    A = {"x1": 0.2, "x2": 0.7, "x3": 1.0}
    B = {"x1": 0.5, "x2": 0.4, "x3": 0.6}
    print("Fuzzy set A:", A)
    print("Fuzzy set B:", B)
    print("\nUnion (A U B):", fuzzy_union(A,B))
    print("Intersection (A ∩ B):", fuzzy_intersection(A,B))
    print("Complement (A'):", fuzzy_complement(A))
    print("Diffrenece (A - B):", fuzzy_difference(A,B))