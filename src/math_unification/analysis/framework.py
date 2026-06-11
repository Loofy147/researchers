import numpy as np
from scipy.spatial.distance import squareform
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.linalg import eigh
import json
from ..data import AXES, FRAMEWORKS, MACRO_AXES

def run_framework_analysis():
    names = list(FRAMEWORKS.keys())
    X = np.array([FRAMEWORKS[n] for n in names])

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

    results = {
        "clusters": {int(k): v for k, v in clusters.items()},
        "embeddings": {name: embedding[i].tolist() for i, name in enumerate(names)},
        "profiles": {name: X[i].tolist() for i, name in enumerate(names)},
        "synergy_pairs": []
    }

    pairs = []
    for i in range(len(names)):
        for j in range(i+1, len(names)):
            if labels[i] != labels[j]:
                pairs.append((names[i], names[j], float(sim[i,j]), int(labels[i]), int(labels[j])))
    pairs.sort(key=lambda x: -x[2])
    results["synergy_pairs"] = [{"n1": p[0], "n2": p[1], "sim": p[2], "c1": p[3], "c2": p[4]} for p in pairs]

    corr_matrix = np.corrcoef(X.T)
    redundancy = []
    for i in range(len(AXES)):
        for j in range(i + 1, len(AXES)):
            if abs(corr_matrix[i, j]) > 0.85:
                redundancy.append((AXES[i], AXES[j], float(corr_matrix[i, j])))
    results["axis_redundancy"] = redundancy

    def calculate_stability(original_labels):
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

    results["cluster_stability"] = calculate_stability(labels)

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

if __name__ == "__main__":
    run_framework_analysis()
