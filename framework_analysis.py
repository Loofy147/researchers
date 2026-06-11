"""
Unified Mathematical Frameworks for Human Phenomena
Computational Analysis Engine
"""

import numpy as np
from scipy.spatial.distance import squareform
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.linalg import eigh
import json

# ── 1. FRAMEWORK CORPUS ──────────────────────────────────────────────────────
AXES = [
    "stochastic_processes", "optimization", "topology", "information_theory",
    "algebra_structure", "dynamical_systems", "geometry", "network_graph",
    "measure_theory", "linear_algebra", "control_theory", "statistical_mechanics",
    "game_theory", "logic_formal", "signal_processing",
]

FRAMEWORKS = {
    "Optimal Control":        [0.3,1.0,0.2,0.4,0.2,0.8,0.5,0.1,0.3,0.8,1.0,0.3,0.5,0.1,0.3],
    "Game Theory":            [0.4,0.9,0.1,0.5,0.5,0.3,0.2,0.6,0.7,0.3,0.2,0.4,1.0,0.5,0.1],
    "Prospect Theory":        [0.6,0.7,0.1,0.4,0.1,0.2,0.2,0.2,0.8,0.2,0.1,0.2,0.8,0.1,0.1],
    "Reinforcement Learning": [0.7,0.9,0.1,0.6,0.2,0.7,0.3,0.4,0.5,0.7,0.8,0.2,0.8,0.1,0.2],
    "Variational Principles": [0.2,1.0,0.5,0.5,0.3,0.8,0.8,0.1,0.5,0.7,0.7,0.5,0.3,0.2,0.4],
    "Bayesian Inference":     [0.8,0.7,0.1,0.9,0.3,0.3,0.3,0.3,1.0,0.5,0.3,0.3,0.5,0.4,0.3],
    "Free Energy Principle":  [0.7,1.0,0.3,0.9,0.3,0.9,0.6,0.3,0.7,0.7,0.8,0.5,0.4,0.2,0.5],
    "Information Geometry":   [0.4,0.7,0.7,0.8,0.5,0.3,1.0,0.2,0.8,0.8,0.2,0.4,0.3,0.2,0.5],
    "Predictive Coding":      [0.6,0.8,0.2,0.8,0.2,0.7,0.4,0.3,0.5,0.6,0.7,0.3,0.3,0.2,0.6],
    "Neural Field Theory":    [0.5,0.6,0.4,0.5,0.3,0.9,0.7,0.4,0.5,0.7,0.5,0.6,0.2,0.1,0.7],
    "Integrated Info Theory": [0.3,0.5,0.4,0.9,0.6,0.6,0.4,0.7,0.5,0.6,0.3,0.5,0.3,0.5,0.2],
    "Global Workspace Theory":[0.3,0.4,0.3,0.7,0.3,0.7,0.3,0.8,0.4,0.5,0.5,0.4,0.3,0.4,0.4],
    "Quantum Cognition":      [0.7,0.5,0.5,0.7,0.8,0.4,0.7,0.3,0.8,0.9,0.2,0.4,0.4,0.5,0.4],
    "Dynamical Systems Psych":[0.4,0.4,0.4,0.4,0.2,1.0,0.5,0.5,0.4,0.5,0.5,0.6,0.2,0.1,0.3],
    "Mean Field Theory":      [0.7,0.7,0.2,0.5,0.3,0.8,0.5,0.5,0.7,0.6,0.4,1.0,0.5,0.1,0.3],
    "Evolutionary Game Theory":[0.6,0.8,0.2,0.6,0.4,0.8,0.3,0.5,0.6,0.4,0.3,0.7,0.9,0.3,0.2],
    "Network Science":        [0.4,0.4,0.6,0.5,0.6,0.6,0.5,1.0,0.5,0.7,0.3,0.5,0.5,0.3,0.2],
    "Social Choice Theory":   [0.3,0.6,0.3,0.4,0.6,0.2,0.2,0.5,0.6,0.3,0.2,0.2,0.8,0.7,0.1],
    "Agent-Based Modeling":   [0.6,0.3,0.2,0.4,0.3,0.8,0.2,0.8,0.4,0.3,0.4,0.6,0.7,0.3,0.2],
    "Category Theory":        [0.1,0.3,0.8,0.4,1.0,0.2,0.7,0.5,0.4,0.6,0.2,0.1,0.3,0.9,0.1],
    "Formal Grammars":        [0.2,0.3,0.5,0.6,0.9,0.3,0.2,0.5,0.3,0.5,0.2,0.1,0.3,1.0,0.3],
    "Algebraic Linguistics":  [0.1,0.3,0.6,0.5,0.9,0.2,0.4,0.4,0.3,0.5,0.1,0.1,0.3,0.9,0.2],
    "Topological Data Anal.": [0.3,0.4,1.0,0.4,0.7,0.3,0.8,0.5,0.5,0.7,0.2,0.2,0.2,0.5,0.2],
    "Stochastic Processes":   [1.0,0.5,0.2,0.6,0.3,0.7,0.3,0.3,0.9,0.6,0.4,0.5,0.3,0.2,0.5],
    "Renormalization Group":  [0.3,0.7,0.5,0.6,0.6,0.7,0.7,0.4,0.5,0.7,0.3,0.9,0.2,0.3,0.4],
    "Gradient Flow Theory":   [0.3,0.9,0.5,0.4,0.3,0.8,0.8,0.2,0.4,0.8,0.6,0.4,0.2,0.1,0.3],
    "Measure-Theoretic Prob.": [0.9,0.4,0.4,0.7,0.5,0.3,0.4,0.2,1.0,0.5,0.2,0.3,0.3,0.5,0.3],
    "Riemannian Geometry":    [0.2,0.7,0.7,0.3,0.5,0.5,1.0,0.2,0.4,0.8,0.5,0.3,0.2,0.2,0.3],
    "Geometric Mechanics":    [0.2,0.8,0.6,0.3,0.6,0.8,0.9,0.2,0.4,0.7,0.7,0.3,0.2,0.2,0.3],
    "Symplectic Geometry":    [0.1,0.8,0.7,0.2,0.6,0.7,0.9,0.1,0.3,0.8,0.6,0.3,0.2,0.3,0.2],
    "Fourier / Wavelet Anal.":[0.3,0.4,0.5,0.7,0.5,0.4,0.5,0.2,0.5,0.9,0.3,0.2,0.1,0.2,1.0],
    "Compressed Sensing":     [0.4,0.8,0.5,0.8,0.4,0.2,0.6,0.2,0.5,0.9,0.3,0.2,0.1,0.3,0.7],
    "Geometric Deep Learning": [0.3,0.9,0.6,0.5,0.4,0.5,0.9,0.7,0.3,0.8,0.3,0.4,0.2,0.4,0.6],
    "Statistical Physics":     [0.8,0.4,0.3,0.5,0.2,0.8,0.4,0.6,0.6,0.5,0.2,1.0,0.4,0.2,0.4],
    "Computational Psychiatry": [0.7,0.8,0.2,0.8,0.2,0.6,0.3,0.4,0.6,0.6,0.7,0.3,0.5,0.2,0.5],
    "Categorical Quantum Mechanics": [0.3,0.4,0.8,0.7,1.0,0.3,0.7,0.5,0.5,0.8,0.2,0.4,0.3,0.9,0.5],
    "Causal Inference":       [0.8,0.5,0.2,0.6,0.4,0.4,0.2,0.5,0.9,0.4,0.3,0.3,0.6,0.7,0.3],
    "Algorithmic Info Theory":[0.2,0.3,0.3,1.0,0.6,0.2,0.3,0.3,0.7,0.4,0.2,0.4,0.2,0.8,0.4],
    "Homotopy Type Theory":   [0.1,0.2,0.9,0.4,1.0,0.2,0.6,0.3,0.3,0.5,0.1,0.1,0.2,1.0,0.2],
    "Evolutionary Dynamics":  [0.7,0.4,0.2,0.5,0.3,0.9,0.3,0.7,0.5,0.4,0.2,0.8,0.9,0.2,0.2],
}

names = list(FRAMEWORKS.keys())
X = np.array([FRAMEWORKS[n] for n in names])

# ── 2. ANALYSIS ─────────────────────────────────────────────────────────────
norms = np.linalg.norm(X, axis=1, keepdims=True)
Xn = X / (norms + 1e-9)
sim = Xn @ Xn.T
dist = np.clip(1 - sim, 0, 2)
np.fill_diagonal(dist, 0)
condensed = squareform(dist)

Z = linkage(condensed, method='ward')
labels = fcluster(Z, t=6, criterion='maxclust')

clusters = {}
for i, name in enumerate(names):
    c = int(labels[i])
    clusters.setdefault(c, []).append(name)

W = np.maximum(sim - np.eye(len(names)), 0)
D = np.diag(W.sum(axis=1))
L = D - W
val, vec = eigh(L)
embedding = vec[:, 1:4]

def bridgeness(idx, sim_matrix, labels_vec):
    own_cluster = labels_vec[idx]
    own_mask = (labels_vec == own_cluster)
    own_mask[idx] = False
    other_mask = ~(labels_vec == own_cluster)
    own_sim = sim_matrix[idx][own_mask].mean() if own_mask.any() else 0
    other_sims = {int(c): float(sim_matrix[idx][labels_vec == c].mean()) for c in np.unique(labels_vec) if c != own_cluster}
    max_other = max(other_sims.values()) if other_sims else 0
    return max_other / (own_sim + 1e-9), other_sims

results = {
    "clusters": {int(k): v for k, v in clusters.items()},
    "embeddings": {name: embedding[i].tolist() for i, name in enumerate(names)},
    "profiles": {name: X[i].tolist() for i, name in enumerate(names)},
    "bridge_candidates": [],
    "cluster_dominance": {},
    "synergy_pairs": []
}

for i, name in enumerate(names):
    bs, _ = bridgeness(i, sim, labels)
    results["bridge_candidates"].append({"name": name, "score": bs, "cluster": int(labels[i])})

for cid in clusters:
    idxs = [names.index(n) for n in clusters[cid]]
    mean_vec = X[idxs].mean(axis=0)
    top2 = np.argsort(mean_vec)[-2:][::-1]
    results["cluster_dominance"][int(cid)] = [AXES[t] for t in top2]

pairs = []
for i in range(len(names)):
    for j in range(i+1, len(names)):
        if labels[i] != labels[j]:
            pairs.append((names[i], names[j], float(sim[i,j]), int(labels[i]), int(labels[j])))
pairs.sort(key=lambda x: -x[2])
results["synergy_pairs"] = [{"n1": p[0], "n2": p[1], "sim": p[2], "c1": p[3], "c2": p[4]} for p in pairs[:10]]

# ── 3. AXIS ORTHOGONALITY VERIFICATION ──────────────────────────────────────
corr_matrix = np.corrcoef(X.T)
results["axis_correlation"] = {
    AXES[i]: {
        AXES[j]: float(corr_matrix[i, j])
        for j in range(len(AXES))
        if i != j
    } for i in range(len(AXES))
}

# Identify highly redundant axes (r > 0.85)
redundancy = []
for i in range(len(AXES)):
    for j in range(i + 1, len(AXES)):
        if abs(corr_matrix[i, j]) > 0.85:
            redundancy.append((AXES[i], AXES[j], float(corr_matrix[i, j])))
results["axis_redundancy"] = redundancy

# ── 4. CLUSTER STABILITY (Leave-One-Out) ────────────────────────────────────
def calculate_stability(data, original_labels):
    cluster_cohesion = {}
    for cid in np.unique(original_labels):
        idxs = np.where(original_labels == cid)[0]
        if len(idxs) > 1:
            c_sim = sim[np.ix_(idxs, idxs)]
            np.fill_diagonal(c_sim, 0)
            cohesion = c_sim.sum() / (len(idxs) * (len(idxs) - 1))
            cluster_cohesion[int(cid)] = float(cohesion)
        else:
            cluster_cohesion[int(cid)] = 1.0
    return cluster_cohesion

results["cluster_stability"] = calculate_stability(X, labels)

# ── 5. META-AXIS ANALYSIS ────────────────────────────────────────────────────
MACRO_AXES = {
    "Symbolic/Formal": ["algebra_structure", "logic_formal", "topology"],
    "Statistical/Prob": ["stochastic_processes", "information_theory", "measure_theory", "statistical_mechanics"],
    "Cybernetic/Control": ["optimization", "dynamical_systems", "control_theory", "game_theory", "signal_processing"],
    "Structural/Geometric": ["geometry", "network_graph", "linear_algebra"]
}

cluster_profiles = {}
for cid in clusters:
    idxs = [names.index(n) for n in clusters[cid]]
    mean_vec = X[idxs].mean(axis=0)
    profile = {}
    for m_name, sub_axes in MACRO_AXES.items():
        sub_idxs = [AXES.index(a) for a in sub_axes]
        profile[m_name] = float(mean_vec[sub_idxs].mean())
    cluster_profiles[int(cid)] = profile
results["meta_axis_profiles"] = cluster_profiles

with open("framework_results.json", "w") as f:
    json.dump(results, f, indent=2)

print("Framework analysis complete. Results saved to framework_results.json.")
