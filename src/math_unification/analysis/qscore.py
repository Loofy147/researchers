import numpy as np
import json
from ..data import AXES, PHENOMENA_PROFILES, CLUSTERS, WEIGHTS, BRIDGES

def run_qscore_analysis():
    try:
        with open("framework_results.json", "r") as f:
            fw_res = json.load(f)
            DYNAMIC_SYNERGIES = fw_res.get("synergy_pairs", [])
            STABILITY = fw_res.get("cluster_stability", {})
            FW_PROFILES = fw_res.get("profiles", {})
            META_PROFILES = fw_res.get("meta_axis_profiles", {})
    except Exception as e:
        print(f"Error loading framework results: {e}")
        return

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
        v1, v2 = np.array(v1), np.array(v2)
        return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2) + 1e-9)

    def calculate_morphism_rigor(n1, n2):
        v1, v2 = np.array(FW_PROFILES.get(n1, [0]*15)), np.array(FW_PROFILES.get(n2, [0]*15))
        idxs = [AXES.index("algebra_structure"), AXES.index("logic_formal"), AXES.index("topology")]
        rigor = (v1[idxs].mean() + v2[idxs].mean()) / 2
        return float(rigor)

    def calculate_conceptual_friction(c1, c2):
        p1 = META_PROFILES.get(str(c1), {})
        p2 = META_PROFILES.get(str(c2), {})
        if not p1 or not p2: return 0.5
        v1 = np.array([p1[k] for k in sorted(p1.keys())])
        v2 = np.array([p2[k] for k in sorted(p2.keys())])
        return float(1 - cosine_sim(v1, v2))

    def calculate_gestalt_consistency(name, cluster_id):
        if name not in FW_PROFILES: return 0.0
        members = []
        for cid_str, info in CLUSTERS.items():
            if cid_str.startswith(f"C{cluster_id}_"):
                members = info["members"]
                break
        if not members: return 0.0
        cluster_vecs = np.array([FW_PROFILES[m] for m in members if m in FW_PROFILES])
        if len(cluster_vecs) == 0: return 0.0
        mean_vec = cluster_vecs.mean(axis=0)
        return float(cosine_sim(FW_PROFILES[name], mean_vec))

    def structural_sensitivity_audit(synergies, fw_profiles):
        if not fw_profiles: return 0.0
        base_top = [s["n1"] + s["n2"] for s in synergies[:10]]
        variances = []
        for _ in range(5):
            perturbed = {k: np.array(v) + np.random.normal(0, 0.05, 15) for k, v in fw_profiles.items()}
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

            target_p = "Emergent Human Behavior"
            for c in CLUSTERS.values():
                if n1 in c["members"]:
                    for p in c["phenomena"]:
                        if p in PHENOMENA_PROFILES:
                            target_p = p
                            break
                    if target_p != "Emergent Human Behavior": break

            synergy_profile = (np.array(FW_PROFILES.get(n1, [0]*15)) + np.array(FW_PROFILES.get(n2, [0]*15))) / 2
            anchor_score = float(cosine_sim(synergy_profile, PHENOMENA_PROFILES.get(target_p, [0]*15)))

            rigor = calculate_morphism_rigor(n1, n2)
            friction = calculate_conceptual_friction(s["c1"], s["c2"])
            g1 = calculate_gestalt_consistency(n1, s["c1"])
            g2 = calculate_gestalt_consistency(n2, s["c2"])
            gestalt = (g1 + g2) / 2

            struct_synergy = None
            if (n1 == "Homotopy Type Theory" and n2 == "Causal Inference") or \
               (n2 == "Homotopy Type Theory" and n1 == "Causal Inference"):
                v1, v2 = np.array(FW_PROFILES[n1]), np.array(FW_PROFILES[n2])
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
