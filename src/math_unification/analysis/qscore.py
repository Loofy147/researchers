import numpy as np
import json
from ..data import AXES, PHENOMENA_PROFILES, CLUSTERS, WEIGHTS, BRIDGES

def run_qscore_analysis():
    try:
        with open("framework_results.json", "r") as f:
            fw_res = json.load(f)
            DYNAMIC_SYNERGIES = fw_res.get("synergy_pairs", [])
            STABILITY = fw_res.get("cluster_stability", {})
            FW_PROFILES_RAW = fw_res.get("profiles", {})
            META_PROFILES_RAW = fw_res.get("meta_axis_profiles", {})
    except Exception as e:
        print(f"Error loading framework results: {e}")
        return

    # Optimization: Pre-convert profiles to numpy arrays
    FW_NAMES = list(FW_PROFILES_RAW.keys())
    FW_X = np.array([FW_PROFILES_RAW[n] for n in FW_NAMES])
    FW_PROFILES = {n: FW_X[i] for i, n in enumerate(FW_NAMES)}
    FW_NAME_TO_IDX = {n: i for i, n in enumerate(FW_NAMES)}

    PH_NAMES = list(PHENOMENA_PROFILES.keys())
    PH_X = np.array([PHENOMENA_PROFILES[n] for n in PH_NAMES])
    PH_NAME_TO_IDX = {n: i for i, n in enumerate(PH_NAMES)}
    PH_PROFILES = {n: PH_X[i] for i, n in enumerate(PH_NAMES)}

    # Pre-calculate normalized versions for cosine similarity
    FW_Xn = FW_X / (np.linalg.norm(FW_X, axis=1, keepdims=True) + 1e-9)
    PH_Xn = PH_X / (np.linalg.norm(PH_X, axis=1, keepdims=True) + 1e-9)

    META_PROFILES = {}
    for cid, p in META_PROFILES_RAW.items():
        META_PROFILES[str(cid)] = np.array([p[k] for k in sorted(p.keys())])

    PREDEFINED_CLUSTER_MEANS = {}
    FW_TO_CLUSTER_MEAN = {}
    FW_TO_PHENOMENON = {}
    FW_TO_PHENOMENON_IDX = {}

    for full_cid, info in CLUSTERS.items():
        try:
            short_id = full_cid.split('_')[0][1:]
            members = info["members"]
            cluster_vecs = [FW_PROFILES[m] for m in members if m in FW_PROFILES]
            if cluster_vecs:
                mean_vec = np.mean(cluster_vecs, axis=0)
                PREDEFINED_CLUSTER_MEANS[short_id] = mean_vec
                for m in members:
                    FW_TO_CLUSTER_MEAN[m] = mean_vec

            target_p = "Emergent Human Behavior"
            for p in info["phenomena"]:
                if p in PH_PROFILES:
                    target_p = p
                    break

            p_idx = PH_NAME_TO_IDX.get(target_p)
            for m in members:
                FW_TO_PHENOMENON[m] = target_p
                FW_TO_PHENOMENON_IDX[m] = p_idx
        except Exception:
            continue

    def q_score(scores):
        return sum(WEIGHTS[k] * v for k, v in scores.items())

    q_results = {}
    for cid, info in CLUSTERS.items():
        q_results[cid] = {
            "q_score": q_score(info["scores"]),
            "human_domain": info["human_domain"],
            "members": info["members"],
            "dominant_axes": info["dominant_axes"],
            "phenomena": info["phenomena"]
        }

    q_vals = [v["q_score"] for v in q_results.values()]
    roadmap_risk = np.std(q_vals) / np.mean(q_vals) if np.mean(q_vals) > 0 else 1.0
    stability_vals = list(STABILITY.values())
    conceptual_cohesion = np.mean(stability_vals) if stability_vals else 0.5
    mean_q = np.mean(q_vals)
    mean_synth = np.mean([b["predicted_synthesis_q"] for b in BRIDGES.values()])
    feasibility = (0.30 * mean_q + 0.30 * mean_synth + 0.25 * conceptual_cohesion + 0.15 * (1 - roadmap_risk))

    # Vectorized audit
    def structural_sensitivity_audit(synergies, X, name_to_idx):
        if X.size == 0 or not synergies: return 0.0
        check_syns = synergies[:50]
        syn_idxs = np.array([(name_to_idx[s["n1"]], name_to_idx[s["n2"]]) for s in check_syns])
        syn_names = [s["n1"] + s["n2"] for s in check_syns]
        base_top = set(syn_names[:10])
        variances = []
        noise = np.random.normal(0, 0.05, (5, X.shape[0], X.shape[1]))
        for i in range(5):
            perturbed_X = X + noise[i]
            norms = np.linalg.norm(perturbed_X, axis=1, keepdims=True)
            perturbed_Xn = perturbed_X / (norms + 1e-9)
            v1s = perturbed_Xn[syn_idxs[:, 0]]
            v2s = perturbed_Xn[syn_idxs[:, 1]]
            sims = np.sum(v1s * v2s, axis=1)
            top_idxs = np.argsort(-sims)[:10]
            new_top = set([syn_names[j] for j in top_idxs])
            intersection = len(base_top & new_top)
            variances.append(1 - (intersection / 10))
        return float(np.mean(variances))

    # Optimization: Fully Vectorized Proposal Generation
    def generate_proposals_vectorized(synergies):
        if not synergies: return []

        # Deduplicate
        unique_syns = []
        seen = set()
        for s in synergies:
            pair = tuple(sorted((s["n1"], s["n2"])))
            if pair not in seen:
                unique_syns.append(s)
                seen.add(pair)

        n = len(unique_syns)
        n1_idxs = np.array([FW_NAME_TO_IDX[s["n1"]] for s in unique_syns])
        n2_idxs = np.array([FW_NAME_TO_IDX[s["n2"]] for s in unique_syns])

        # 1. Anchor Score (Cosine Similarity between Synergy Profile and Target Phenomenon)
        syn_profiles = (FW_X[n1_idxs] + FW_X[n2_idxs]) / 2
        syn_profiles_n = syn_profiles / (np.linalg.norm(syn_profiles, axis=1, keepdims=True) + 1e-9)

        ph_idxs = np.array([FW_TO_PHENOMENON_IDX.get(s["n1"], 0) for s in unique_syns])
        anchor_scores = np.sum(syn_profiles_n * PH_Xn[ph_idxs], axis=1)

        # 2. Morphism Rigor
        m_idxs = [AXES.index("algebra_structure"), AXES.index("logic_formal"), AXES.index("topology")]
        rigor = (FW_X[n1_idxs][:, m_idxs].mean(axis=1) + FW_X[n2_idxs][:, m_idxs].mean(axis=1)) / 2

        # 3. Conceptual Friction
        # (This remains largely dictionary based because of meta-profiles, but we can vectorize cosine_sim)
        frictions = []
        for s in unique_syns:
            p1 = META_PROFILES.get(str(s["c1"]))
            p2 = META_PROFILES.get(str(s["c2"]))
            if p1 is None or p2 is None: frictions.append(0.5)
            else:
                sim = np.dot(p1, p2) / (np.linalg.norm(p1) * np.linalg.norm(p2) + 1e-9)
                frictions.append(1 - sim)
        frictions = np.array(frictions)

        # 4. Gestalt Consistency
        def get_gestalt_batch(idxs):
            # cosine_sim between framework and its cluster mean
            fw_n = FW_Xn[idxs]
            means = np.array([FW_TO_CLUSTER_MEAN.get(FW_NAMES[i], np.zeros(15)) for i in idxs])
            # normalize means
            means_n = means / (np.linalg.norm(means, axis=1, keepdims=True) + 1e-9)
            return np.sum(fw_n * means_n, axis=1)

        gestalt = (get_gestalt_batch(n1_idxs) + get_gestalt_batch(n2_idxs)) / 2

        # 5. Priority Score
        sims = np.array([s["sim"] for s in unique_syns])
        priority_scores = sims * 0.4 + anchor_scores * 0.2 + rigor * 0.2 + gestalt * 0.3 - frictions * 0.1

        proposals = []
        for i, s in enumerate(unique_syns):
            n1, n2 = s["n1"], s["n2"]
            struct_synergy = None
            if (n1 == "Homotopy Type Theory" and n2 == "Causal Inference") or                (n2 == "Homotopy Type Theory" and n1 == "Causal Inference"):
                v1, v2 = FW_X[n1_idxs[i]], FW_X[n2_idxs[i]]
                struct_synergy = float(np.sum(np.minimum(v1, v2)) / np.sum(np.maximum(v1, v2) + 1e-9))
                title = f"FRONTIVE BRIDGE: {n1} × {n2}"
            else:
                title = f"Synthesis: {n1} × {n2}"

            # Validation Audit
            v_score = rigor[i] * gestalt[i]
            if v_score > 0.75:
                validation = "PASSED: Strong Functorial Candidate"
            elif v_score > 0.55:
                validation = "PROVISIONAL: Commutative Diagram Identified"
            else:
                validation = "SPECULATIVE: Morphism Not Yet Formalized"

            # Hypothesis Generation
            hypothesis = f"Unification of {n1} and {n2} formalizes the underlying invariants of {FW_TO_PHENOMENON.get(n1,  'Emergent Human Behavior')}."

            proposals.append({
                "validation_audit": validation,
                "core_hypothesis": hypothesis,
                "title": title,
                "sim": float(sims[i]),
                "c1": s["c1"],
                "c2": s["c2"],
                "target_phenomenon": FW_TO_PHENOMENON.get(n1,  'Emergent Human Behavior'),
                "anchor_score": float(anchor_scores[i]),
                "morphism_rigor": float(rigor[i]),
                "conceptual_friction": float(frictions[i]),
                "gestalt_consistency": float(gestalt[i]),
                "priority_score": float(priority_scores[i]),
                "structural_synergy": struct_synergy
            })
        return proposals

    all_proposals = generate_proposals_vectorized(DYNAMIC_SYNERGIES)
    sensitivity = structural_sensitivity_audit(DYNAMIC_SYNERGIES, FW_X, FW_NAME_TO_IDX)

    frontiers = sorted(all_proposals, key=lambda x: -x["priority_score"])[:12]
    niche_breakthroughs = [p for p in all_proposals if 0.5 <= p["sim"] <= 0.85 and p["anchor_score"] > 0.85]

    with open("qscore_results.json", "w") as f:
        json.dump({
            "cluster_results": q_results,
            "bridges": BRIDGES,
            "research_frontiers": frontiers,
            "niche_breakthroughs": niche_breakthroughs,
            "metrics": {
                "mean_cluster_q": mean_q,
                "mean_bridge_q": mean_synth,
                "roadmap_risk": float(roadmap_risk),
                "conceptual_cohesion": float(conceptual_cohesion),
                "feasibility": float(feasibility),
                "structural_sensitivity": sensitivity
            }
        }, f, indent=2)

    print("Q-score analysis complete. Results saved to qscore_results.json.")

if __name__ == "__main__":
    run_qscore_analysis()
