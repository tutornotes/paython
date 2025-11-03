
def fuzzy_union(A, B):
    return {x: max(A.get(x, 0), B.get(x, 0)) for x in sorted(set(A) | set(B))}

def fuzzy_intersection(A, B):
    return {x: min(A.get(x, 0), B.get(x, 0)) for x in sorted(set(A) | set(B))}

def fuzzy_complement(A):
    return {x: 1 - A[x] for x in A}

def de_morgan_laws(A, B):
    """Check De Morgan's law for fuzzy set A and B"""
    lhs1 = fuzzy_complement(fuzzy_union(A, B))
    rhs1 = fuzzy_intersection(fuzzy_complement(A), fuzzy_complement(B))
    lhs2 = fuzzy_complement(fuzzy_intersection(A, B))
    rhs2 = fuzzy_union(fuzzy_complement(A), fuzzy_complement(B))
    return lhs1 == rhs1 and lhs2 == rhs2

if __name__ == "__main__":
    A = {"x1": 0.2, "x2": 0.7, "x3": 1.0}
    B = {"x1": 0.5, "x2": 0.4, "x3": 0.6}
    result1 = de_morgan_laws(A, B)
    print("De Morgan's law verification:")
    print(f"(A U B)' == (A' ∩ B'): {result1}")
