"""
Unified Mathematical Frameworks for Human Phenomena
Computational Analysis Engine
"""

import numpy as np
from scipy.spatial.distance import squareform
from scipy.cluster.hierarchy import linkage, fcluster, dendrogram
from scipy.linalg import eigh
import json

# ── 1. FRAMEWORK CORPUS ──────────────────────────────────────────────────────
# 32 mathematical frameworks, each encoded as a feature vector over shared
# conceptual axes (0=absent, 1=present, partial values allowed)

AXES = [
    "stochastic_processes",   # randomness / uncertainty formalism
    "optimization",           # variational / extremal principles
    "topology",               # shape / continuity / invariants
    "information_theory",     # entropy / coding / compression
    "algebra_structure",      # groups / categories / symmetry
    "dynamical_systems",      # flows / attractors / bifurcations
    "geometry",               # manifolds / curvature / distance
    "network_graph",          # nodes / edges / adjacency
    "measure_theory",         # integration / probability spaces
    "linear_algebra",         # eigensystems / spectral methods
    "control_theory",         # feedback / stability / regulation
    "statistical_mechanics",  # ensembles / phase transitions
    "game_theory",            # agents / strategies / equilibria
    "logic_formal",           # syntax / semantics / proof
    "signal_processing",      # Fourier / wavelets / filters
]

FRAMEWORKS = {
    # ── AGENCY & DECISION ───
    "Optimal Control":        [0.3,1.0,0.2,0.4,0.2,0.8,0.5,0.1,0.3,0.8,1.0,0.3,0.5,0.1,0.3],
    "Game Theory":            [0.4,0.9,0.1,0.5,0.5,0.3,0.2,0.6,0.7,0.3,0.2,0.4,1.0,0.5,0.1],
    "Prospect Theory":        [0.6,0.7,0.1,0.4,0.1,0.2,0.2,0.2,0.8,0.2,0.1,0.2,0.8,0.1,0.1],
    "Reinforcement Learning": [0.7,0.9,0.1,0.6,0.2,0.7,0.3,0.4,0.5,0.7,0.8,0.2,0.8,0.1,0.2],
    "Variational Principles": [0.2,1.0,0.5,0.5,0.3,0.8,0.8,0.1,0.5,0.7,0.7,0.5,0.3,0.2,0.4],
    # ── COGNITION & INFERENCE ───
    "Bayesian Inference":     [0.8,0.7,0.1,0.9,0.3,0.3,0.3,0.3,1.0,0.5,0.3,0.3,0.5,0.4,0.3],
    "Free Energy Principle":  [0.7,1.0,0.3,0.9,0.3,0.9,0.6,0.3,0.7,0.7,0.8,0.5,0.4,0.2,0.5],
    "Information Geometry":   [0.4,0.7,0.7,0.8,0.5,0.3,1.0,0.2,0.8,0.8,0.2,0.4,0.3,0.2,0.5],
    "Predictive Coding":      [0.6,0.8,0.2,0.8,0.2,0.7,0.4,0.3,0.5,0.6,0.7,0.3,0.3,0.2,0.6],
    "Neural Field Theory":    [0.5,0.6,0.4,0.5,0.3,0.9,0.7,0.4,0.5,0.7,0.5,0.6,0.2,0.1,0.7],
    # ── CONSCIOUSNESS & INTEGRATION ───
    "Integrated Info Theory": [0.3,0.5,0.4,0.9,0.6,0.6,0.4,0.7,0.5,0.6,0.3,0.5,0.3,0.5,0.2],
    "Global Workspace Theory":[0.3,0.4,0.3,0.7,0.3,0.7,0.3,0.8,0.4,0.5,0.5,0.4,0.3,0.4,0.4],
    "Quantum Cognition":      [0.7,0.5,0.5,0.7,0.8,0.4,0.7,0.3,0.8,0.9,0.2,0.4,0.4,0.5,0.4],
    "Dynamical Systems Psych":[0.4,0.4,0.4,0.4,0.2,1.0,0.5,0.5,0.4,0.5,0.5,0.6,0.2,0.1,0.3],
    # ── SOCIAL & COLLECTIVE ───
    "Mean Field Theory":      [0.7,0.7,0.2,0.5,0.3,0.8,0.5,0.5,0.7,0.6,0.4,1.0,0.5,0.1,0.3],
    "Evolutionary Game Theory":[0.6,0.8,0.2,0.6,0.4,0.8,0.3,0.5,0.6,0.4,0.3,0.7,0.9,0.3,0.2],
    "Network Science":        [0.4,0.4,0.6,0.5,0.6,0.6,0.5,1.0,0.5,0.7,0.3,0.5,0.5,0.3,0.2],
    "Social Choice Theory":   [0.3,0.6,0.3,0.4,0.6,0.2,0.2,0.5,0.6,0.3,0.2,0.2,0.8,0.7,0.1],
    "Agent-Based Modeling":   [0.6,0.3,0.2,0.4,0.3,0.8,0.2,0.8,0.4,0.3,0.4,0.6,0.7,0.3,0.2],
    # ── LANGUAGE & STRUCTURE ───
    "Category Theory":        [0.1,0.3,0.8,0.4,1.0,0.2,0.7,0.5,0.4,0.6,0.2,0.1,0.3,0.9,0.1],
    "Formal Grammars":        [0.2,0.3,0.5,0.6,0.9,0.3,0.2,0.5,0.3,0.5,0.2,0.1,0.3,1.0,0.3],
    "Algebraic Linguistics":  [0.1,0.3,0.6,0.5,0.9,0.2,0.4,0.4,0.3,0.5,0.1,0.1,0.3,0.9,0.2],
    "Topological Data Anal.": [0.3,0.4,1.0,0.4,0.7,0.3,0.8,0.5,0.5,0.7,0.2,0.2,0.2,0.5,0.2],
    # ── TEMPORAL & ADAPTIVE ───
    "Stochastic Processes":   [1.0,0.5,0.2,0.6,0.3,0.7,0.3,0.3,0.9,0.6,0.4,0.5,0.3,0.2,0.5],
    "Renormalization Group":  [0.3,0.7,0.5,0.6,0.6,0.7,0.7,0.4,0.5,0.7,0.3,0.9,0.2,0.3,0.4],
    "Gradient Flow Theory":   [0.3,0.9,0.5,0.4,0.3,0.8,0.8,0.2,0.4,0.8,0.6,0.4,0.2,0.1,0.3],
    "Measure-Theoretic Prob.": [0.9,0.4,0.4,0.7,0.5,0.3,0.4,0.2,1.0,0.5,0.2,0.3,0.3,0.5,0.3],
    # ── EMBODIMENT & MOTOR ───
    "Riemannian Geometry":    [0.2,0.7,0.7,0.3,0.5,0.5,1.0,0.2,0.4,0.8,0.5,0.3,0.2,0.2,0.3],
    "Geometric Mechanics":    [0.2,0.8,0.6,0.3,0.6,0.8,0.9,0.2,0.4,0.7,0.7,0.3,0.2,0.2,0.3],
    "Symplectic Geometry":    [0.1,0.8,0.7,0.2,0.6,0.7,0.9,0.1,0.3,0.8,0.6,0.3,0.2,0.3,0.2],
    # ── SIGNAL & PERCEPTION ───
    "Fourier / Wavelet Anal.":[0.3,0.4,0.5,0.7,0.5,0.4,0.5,0.2,0.5,0.9,0.3,0.2,0.1,0.2,1.0],
    "Compressed Sensing":     [0.4,0.8,0.5,0.8,0.4,0.2,0.6,0.2,0.5,0.9,0.3,0.2,0.1,0.3,0.7],
}

names = list(FRAMEWORKS.keys())
X = np.array([FRAMEWORKS[n] for n in names])   # shape (32, 15)

# ── 2. COSINE DISTANCE MATRIX ─────────────────────────────────────────────
norms = np.linalg.norm(X, axis=1, keepdims=True)
Xn = X / norms
sim = Xn @ Xn.T
dist = np.clip(1 - sim, 0, 2)
np.fill_diagonal(dist, 0)
condensed = squareform(dist)

# ── 3. HIERARCHICAL CLUSTERING (Ward) ────────────────────────────────────
Z = linkage(condensed, method='ward')
labels = fcluster(Z, t=6, criterion='maxclust')   # 6 thematic groups

clusters = {}
for i, name in enumerate(names):
    c = int(labels[i])
    clusters.setdefault(c, []).append(name)

print("=== THEMATIC CLUSTERS ===")
cluster_names = {
    1: None, 2: None, 3: None, 4: None, 5: None, 6: None
}
for cid in sorted(clusters):
    print(f"\nCluster {cid}: {clusters[cid]}")

# ── 4. SPECTRAL EMBEDDING (top 3 eigenvectors of Laplacian) ───────────────
# Graph Laplacian from similarity
W = np.maximum(sim - np.eye(len(names)), 0)   # adjacency, no self-loops
D = np.diag(W.sum(axis=1))
L = D - W
eigenvalues, eigenvectors = eigh(L)
# Take eigenvectors 1-3 (skip trivial 0th)
embedding = eigenvectors[:, 1:4]

print("\n=== SPECTRAL EMBEDDING (first 3 non-trivial dims) ===")
for i, name in enumerate(names):
    e = embedding[i]
    print(f"  {name:35s} [{e[0]:+.3f}, {e[1]:+.3f}, {e[2]:+.3f}]  cluster={labels[i]}")

# ── 5. BRIDGE CONCEPT DETECTION ──────────────────────────────────────────
# A bridge concept is a framework that has HIGH similarity to multiple clusters
def bridgeness(idx, sim_matrix, labels_vec):
    """Ratio of max inter-cluster sim to within-cluster sim."""
    own_cluster = labels_vec[idx]
    own_mask = (labels_vec == own_cluster)
    own_mask[idx] = False
    other_mask = ~(labels_vec == own_cluster)

    own_sim = sim_matrix[idx][own_mask].mean() if own_mask.any() else 0
    other_sims = {}
    for c in np.unique(labels_vec):
        if c == own_cluster: continue
        cmask = labels_vec == c
        other_sims[c] = sim_matrix[idx][cmask].mean()

    max_other = max(other_sims.values()) if other_sims else 0
    bridge_score = max_other / (own_sim + 1e-9)
    return bridge_score, other_sims

print("\n=== BRIDGE CANDIDATES (inter/intra sim ratio) ===")
bridge_scores = []
for i, name in enumerate(names):
    bs, os = bridgeness(i, sim, labels)
    bridge_scores.append((name, bs, labels[i]))

bridge_scores.sort(key=lambda x: -x[1])
for name, bs, cl in bridge_scores[:8]:
    print(f"  {name:35s}  bridge_score={bs:.3f}  cluster={cl}")

# ── 6. AXIS DOMINANCE per CLUSTER ─────────────────────────────────────────
print("\n=== DOMINANT AXES per CLUSTER ===")
for cid in sorted(clusters):
    idxs = [names.index(n) for n in clusters[cid]]
    mean_vec = X[idxs].mean(axis=0)
    top2 = np.argsort(mean_vec)[-2:][::-1]
    print(f"  Cluster {cid}: {[AXES[t] for t in top2]}  —  members: {len(clusters[cid])}")

# ── 7. PAIRWISE SYNERGY MATRIX (top framework pairs across clusters) ───────
print("\n=== TOP CROSS-CLUSTER SYNERGY PAIRS ===")
pairs = []
for i in range(len(names)):
    for j in range(i+1, len(names)):
        if labels[i] != labels[j]:
            pairs.append((names[i], names[j], float(sim[i,j]), labels[i], labels[j]))
pairs.sort(key=lambda x: -x[2])
for n1, n2, s, c1, c2 in pairs[:10]:
    print(f"  {n1:30s} <-> {n2:30s}  sim={s:.3f}  [{c1}↔{c2}]")
