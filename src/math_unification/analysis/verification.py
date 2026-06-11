import numpy as np
from ..data import AXES

def verify_morphism_alignment(v1, v2):
    """
    Analyzes two framework vectors to identify basis and bridging axes for a potential morphism.
    """
    v1 = np.array(v1)
    v2 = np.array(v2)

    # Basis Axes: High scores in both frameworks (> 0.7)
    basis_indices = np.where((v1 > 0.7) & (v2 > 0.7))[0]
    basis_axes = [AXES[i] for i in basis_indices]

    # Bridging Axes: Where one is high (> 0.8) and the other is low (< 0.4)
    # This represents complementary strengths.
    bridge12 = np.where((v1 > 0.8) & (v2 < 0.4))[0]
    bridge21 = np.where((v2 > 0.8) & (v1 < 0.4))[0]

    bridging_axes = [AXES[i] for i in np.concatenate([bridge12, bridge21])]

    # Proof of Concept Score:
    # High shared basis (rigor) + complementary bridging (utility)
    poc_score = (len(basis_axes) * 0.15 + len(bridging_axes) * 0.1)
    poc_score = min(poc_score, 1.0)

    return {
        "basis_axes": basis_axes,
        "bridging_axes": bridging_axes,
        "poc_score": float(poc_score)
    }

if __name__ == "__main__":
    # Simple test
    test_v1 = [1.0, 0.2, 0.9, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    test_v2 = [0.9, 0.1, 1.0, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    print(verify_morphism_alignment(test_v1, test_v2))
