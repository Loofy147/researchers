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
    FW_PROFILES = {k: np.array(v) for k, v in FW_PROFILES_RAW.items()}
    PH_PROFILES = {k: np.array(v) for k, v in PHENOMENA_PROFILES.items()}

    # Optimization: Pre-calculate meta-axis profiles as arrays
    META_PROFILES = {}
    for cid, p in META_PROFILES_RAW.items():
        META_PROFILES[str(cid)] = np.array([p[k] for k in sorted(p.keys())])

    # Optimization: Pre-calculate cluster means for Gestalt Consistency
    # Map numeric ID (e.g., "1") to the mean of members in that predefined cluster
    PREDEFINED_CLUSTER_MEANS = {}
    for full_cid, info in CLUSTERS.items():
        try:
            # Extract "1" from "C1_..."
            short_id = full_cid.split('_')[0][1:]
            members = info["members"]
            cluster_vecs = [FW_PROFILES[m] for m in members if m in FW_PROFILES]
            if cluster_vecs:
                PREDEFINED_CLUSTER_MEANS[short_id] = np.mean(cluster_vecs, axis=0)
        except Exception:
            continue

    # Optimization: Map frameworks to their target phenomena based on CLUSTERS membership
    FW_TO_PHENOMENON = {}
    for full_cid, info in CLUSTERS.items():
        target_p = "Emergent Human Behavior"
        for p in info["phenomena"]:
            if p in PH_PROFILES:
                target_p = p
                break
        for m in info["members"]:
            FW_TO_PHENOMENON[m] = target_p

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

    def cosine_sim(v1, v2):
        return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2) + 1e-9)

    def calculate_morphism_rigor(n1, n2):
        v1 = FW_PROFILES.get(n1, np.zeros(15))
        v2 = FW_PROFILES.get(n2, np.zeros(15))
        idxs = [AXES.index("algebra_structure"), AXES.index("logic_formal"), AXES.index("topology")]
        rigor = (v1[idxs].mean() + v2[idxs].mean()) / 2
        return float(rigor)

    def calculate_conceptual_friction(c1, c2):
        p1 = META_PROFILES.get(str(c1))
        p2 = META_PROFILES.get(str(c2))
        if p1 is None or p2 is None: return 0.5
        return float(1 - cosine_sim(p1, p2))

    def calculate_gestalt_consistency(name, cluster_id):
        if name not in FW_PROFILES: return 0.0
        mean_vec = PREDEFINED_CLUSTER_MEANS.get(str(cluster_id))
        if mean_vec is None: return 0.0
        return float(cosine_sim(FW_PROFILES[name], mean_vec))

    def structural_sensitivity_audit(synergies, fw_profiles):
        if not fw_profiles: return 0.0
        base_top = [s["n1"] + s["n2"] for s in synergies[:10]]
        variances = []
        for _ in range(5):
            perturbed = {k: v + np.random.normal(0, 0.05, 15) for k, v in fw_profiles.items()}
            new_syns = []
            for s in synergies[:50]:
                v1, v2 = perturbed[s["n1"]], perturbed[s["n2"]]
                sim = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2) + 1e-9)
                new_syns.append({"name": s["n1"] + s["n2"], "sim": sim})
            new_syns.sort(key=lambda x: -x["sim"])
            new_top = [x["name"] for x in new_syns[:10]]
            intersection = len(set(base_top) & set(new_top))
            variances.append(1 - (intersection / 10))
        return float(np.mean(variances))

    def generate_proposals():
        proposals = []
        seen_pairs = set()

        for s in DYNAMIC_SYNERGIES:
            n1, n2 = s["n1"], s["n2"]
            if (n1, n2) in seen_pairs or (n2, n1) in seen_pairs: continue

            target_p = FW_TO_PHENOMENON.get(n1, "Emergent Human Behavior")

            v1, v2 = FW_PROFILES.get(n1, np.zeros(15)), FW_PROFILES.get(n2, np.zeros(15))
            synergy_profile = (v1 + v2) / 2
            anchor_score = float(cosine_sim(synergy_profile, PH_PROFILES.get(target_p, np.zeros(15))))

            rigor = calculate_morphism_rigor(n1, n2)
            friction = calculate_conceptual_friction(s["c1"], s["c2"])
            g1 = calculate_gestalt_consistency(n1, s["c1"])
            g2 = calculate_gestalt_consistency(n2, s["c2"])
            gestalt = (g1 + g2) / 2

            struct_synergy = None
            if (n1 == "Homotopy Type Theory" and n2 == "Causal Inference") or                (n2 == "Homotopy Type Theory" and n1 == "Causal Inference"):
                struct_synergy = float(np.sum(np.minimum(v1, v2)) / np.sum(np.maximum(v1, v2) + 1e-9))
                title = f"FRONTIVE BRIDGE: {n1} × {n2}"
            else:
                title = f"Synthesis: {n1} × {n2}"

            prop = {
                "title": title,
                "sim": s["sim"],
                "c1": s["c1"],
                "c2": s["c2"],
                "target_phenomenon": target_p,
                "anchor_score": anchor_score,
                "morphism_rigor": rigor,
                "conceptual_friction": friction,
                "gestalt_consistency": gestalt,
                "priority_score": float(s["sim"] * 0.4 + anchor_score * 0.2 + rigor * 0.2 + gestalt * 0.3 - friction * 0.1),
                "structural_synergy": struct_synergy
            }
            proposals.append(prop)
            seen_pairs.add((n1, n2))
        return proposals

    all_proposals = generate_proposals()
    sensitivity = structural_sensitivity_audit(DYNAMIC_SYNERGIES, FW_PROFILES)

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
