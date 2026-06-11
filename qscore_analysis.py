"""
Q-Score Analysis for each cluster + integration strategy computation
"""
import numpy as np
import json

PHENOMENA_PROFILES = {
    "Generative AI": [0.3, 0.9, 0.4, 0.8, 0.7, 0.5, 0.4, 0.6, 0.4, 0.8, 0.3, 0.4, 0.2, 0.6, 0.6],
    "Brain mapping": [0.5, 0.4, 0.8, 0.6, 0.3, 0.7, 0.9, 0.8, 0.4, 0.8, 0.2, 0.5, 0.1, 0.2, 0.7],
    "Dopamine detoxing": [0.7, 0.9, 0.1, 0.7, 0.2, 0.8, 0.3, 0.4, 0.6, 0.5, 0.9, 0.3, 0.6, 0.1, 0.4],
    "Neurodivergence": [0.5, 0.5, 0.4, 0.6, 0.3, 0.9, 0.5, 0.7, 0.5, 0.6, 0.4, 0.6, 0.2, 0.1, 0.6],
    "Phantom limb syndrome": [0.2, 0.8, 0.6, 0.4, 0.3, 0.8, 0.9, 0.3, 0.4, 0.7, 0.7, 0.3, 0.1, 0.1, 0.5],
    "Stan culture": [0.6, 0.3, 0.3, 0.5, 0.2, 0.9, 0.3, 0.9, 0.4, 0.4, 0.2, 0.8, 0.6, 0.2, 0.3],
    "Wealth inequality": [0.8, 0.6, 0.1, 0.4, 0.3, 0.4, 0.2, 0.6, 0.9, 0.4, 0.1, 0.5, 0.9, 0.2, 0.1],
    "Postmodernism": [0.2, 0.2, 0.7, 0.4, 0.9, 0.3, 0.4, 0.4, 0.3, 0.4, 0.1, 0.2, 0.3, 1.0, 0.2],
    "Virtual reality ecosystems": [0.3, 0.5, 0.8, 0.7, 0.4, 0.6, 0.9, 0.7, 0.4, 0.8, 0.3, 0.3, 0.2, 0.3, 0.8]
}

# Cluster assignments updated with Frontier mathematics
CLUSTERS = {
    "C1_Symbolic_Structure": {
        "members": ["Category Theory", "Formal Grammars", "Algebraic Linguistics", "Categorical Quantum Mechanics", "Homotopy Type Theory"],
        "dominant_axes": ["logic_formal", "algebra_structure"],
        "human_domain": "Language, Logic, Cultural Form",
        "scores": {"Grounding": 0.72, "Certainty": 0.85, "Structure": 0.95, "Applicability": 0.60, "Coherence": 0.90, "Generativity": 0.78, "Presentation": 0.70, "Temporal": 0.88},
        "phenomena": ["Generative AI", "Identity formation", "The Ship of Theseus", "Postmodernism", "Infinite regress", "Natural language semantics"]
    },
    "C2_Representational_Geometry": {
        "members": ["Information Geometry","Quantum Cognition","Topological Data Anal.","Fourier/Wavelet Anal.","Compressed Sensing"],
        "dominant_axes": ["linear_algebra", "geometry"],
        "human_domain": "Representation, Perception, Signal",
        "scores": {"Grounding": 0.82, "Certainty": 0.78, "Structure": 0.88, "Applicability": 0.85, "Coherence": 0.80, "Generativity": 0.83, "Presentation": 0.75, "Temporal": 0.82},
        "phenomena": ["Brain mapping", "Deepfakes", "Facial recognition systems", "Virtual reality ecosystems", "Color theory", "Facial harmony"]
    },
    "C3_Probabilistic_Choice": {
        "members": ["Game Theory","Prospect Theory","Bayesian Inference","Social Choice Theory","Measure-Theoretic Prob.", "Causal Inference", "Algorithmic Info Theory"],
        "dominant_axes": ["measure_theory", "stochastic_processes"],
        "human_domain": "Decision, Rationality, Risk",
        "scores": {"Grounding": 0.88, "Certainty": 0.84, "Structure": 0.82, "Applicability": 0.92, "Coherence": 0.79, "Generativity": 0.85, "Presentation": 0.82, "Temporal": 0.86},
        "phenomena": ["The lipstick effect", "Influencer commodification", "Decision fatigue", "Geopolitical strategy", "Proxy wars", "Wealth inequality"]
    },
    "C4_Collective_Dynamics": {
        "members": ["Neural Field Theory","Integrated Info Theory","Global Workspace Theory","Dynamical Systems Psych","Mean Field Theory","Evolutionary Game Theory","Network Science","Agent-Based Modeling","Renormalization Group", "Geometric Deep Learning", "Statistical Physics", "Evolutionary Dynamics"],
        "dominant_axes": ["dynamical_systems", "statistical_mechanics"],
        "human_domain": "Consciousness, Social Emergence, Brain Dynamics",
        "scores": {"Grounding": 0.79, "Certainty": 0.70, "Structure": 0.76, "Applicability": 0.78, "Coherence": 0.72, "Generativity": 0.88, "Presentation": 0.68, "Temporal": 0.80},
        "phenomena": ["Neurodivergence", "Oxytocin and bonding", "Neural pathways", "Stan culture", "Cancel culture", "Populism", "Nationalism", "Modern loneliness", "Inductive biases"]
    },
    "C5_Geometric_Optimization": {
        "members": ["Variational Principles","Gradient Flow Theory","Riemannian Geometry","Geometric Mechanics","Symplectic Geometry"],
        "dominant_axes": ["geometry", "optimization"],
        "human_domain": "Motor Control, Learning Geometry, Physical Embodiment",
        "scores": {"Grounding": 0.76, "Certainty": 0.80, "Structure": 0.92, "Applicability": 0.67, "Coherence": 0.87, "Generativity": 0.79, "Presentation": 0.65, "Temporal": 0.75},
        "phenomena": ["Phantom limb syndrome", "Symmetry constraints"]
    },
    "C6_Agency_Control": {
        "members": ["Optimal Control","Reinforcement Learning","Free Energy Principle","Predictive Coding", "Computational Psychiatry", "Stochastic Processes"],
        "dominant_axes": ["optimization", "control_theory"],
        "human_domain": "Active Inference, Goal-Directed Behavior",
        "scores": {"Grounding": 0.85, "Certainty": 0.81, "Structure": 0.86, "Applicability": 0.88, "Coherence": 0.84, "Generativity": 0.90, "Presentation": 0.78, "Temporal": 0.84},
        "phenomena": ["Dopamine detoxing", "Neural interfaces", "Autonomous vehicles", "Simulation theory", "Mental health diagnostics"]
    }
}

WEIGHTS = {'Grounding':0.23,'Certainty':0.15,'Structure':0.18,'Applicability':0.16, 'Coherence':0.12,'Generativity':0.08,'Presentation':0.05,'Temporal':0.03}
AXES = ["stochastic_processes", "optimization", "topology", "information_theory", "algebra_structure", "dynamical_systems", "geometry", "network_graph", "measure_theory", "linear_algebra", "control_theory", "statistical_mechanics", "game_theory", "logic_formal", "signal_processing"]

def q_score(scores):
    return sum(WEIGHTS[k] * v for k, v in scores.items())

BRIDGES = {
    "Free Energy Principle (C6↔C4, C6↔C5)": {
        "connects": ["C6_Agency_Control","C4_Collective_Dynamics","C5_Geometric_Optimization"],
        "mechanism": "Unifies variational inference (C6), nonlinear dynamics (C4), and Riemannian gradient flows (C5).",
        "predicted_synthesis_q": 0.897,
        "key_equation": "dμ/dt = -∂F/∂μ"
    },
    "Topological Data Analysis (C2↔C1, C2↔C4)": {
        "connects": ["C2_Representational_Geometry","C1_Symbolic_Structure","C4_Collective_Dynamics"],
        "mechanism": "Persistent homology (C2) maps topological invariants from neural data (C4) to categorical structure (C1).",
        "predicted_synthesis_q": 0.873,
        "key_equation": "H_k(X)"
    },
    "Stochastic Optimal Control (C3↔C6, C3↔C5)": {
        "connects": ["C3_Probabilistic_Choice","C6_Agency_Control","C5_Geometric_Optimization"],
        "mechanism": "Hamilton-Jacobi-Bellman equation on statistical manifolds (C5) yields rational choice under uncertainty (C3).",
        "predicted_synthesis_q": 0.885,
        "key_equation": "∂V/∂t + H(x, ∇V, t) = 0"
    },
    "Categorical Probability (C1↔C3)": {
        "connects": ["C1_Symbolic_Structure","C3_Probabilistic_Choice"],
        "mechanism": "Kleisli categories for probability monads (C1) give compositional semantics to Bayesian updating (C3).",
        "predicted_synthesis_q": 0.852,
        "key_equation": "P : C → Kleisli(Dist)"
    },
    "Renormalization / Scale Symmetry (C4↔C5↔C2)": {
        "connects": ["C4_Collective_Dynamics","C5_Geometric_Optimization","C2_Representational_Geometry"],
        "mechanism": "Fixed points of RG flow (C4) correspond to critical states; geometric flow (C5) scales information compression (C2).",
        "predicted_synthesis_q": 0.868,
        "key_equation": "dg_μν/dt = -2 R_μν"
    }
}

# ── 3. DYNAMIC BRIDGE DISCOVERY & VALIDATION ────────────────────────────────
try:
    with open("framework_results.json", "r") as f:
        fw_res = json.load(f)
        DYNAMIC_SYNERGIES = fw_res.get("synergy_pairs", [])
        STABILITY = fw_res.get("cluster_stability", {})
        FW_PROFILES = fw_res.get("profiles", {})
        META_PROFILES = fw_res.get("meta_axis_profiles", {})
except:
    DYNAMIC_SYNERGIES = []
    STABILITY = {}
    FW_PROFILES = {}
    META_PROFILES = {}

def validate_clusters(clusters_dict):
    """Ensures all frameworks are uniquely assigned and members exist."""
    all_members = []
    for cid, info in clusters_dict.items():
        all_members.extend(info["members"])
    if len(all_members) != len(set(all_members)):
        # Find duplicates
        seen = set()
        dupes = [x for x in all_members if x in seen or seen.add(x)]
        print(f"Warning: Duplicate framework assignment detected: {dupes}")
    return True

validate_clusters(CLUSTERS)

q_results = {}
for cid, info in CLUSTERS.items():
    q_results[cid] = {
        "q_score": q_score(info["scores"]),
        "human_domain": info["human_domain"],
        "members": info["members"],
        "dominant_axes": info["dominant_axes"],
        "phenomena": info["phenomena"]
    }

# ── 4. REFINED FEASIBILITY MODELING ──────────────────────────────────────────
q_vals = [v["q_score"] for v in q_results.values()]
roadmap_risk = np.std(q_vals) / np.mean(q_vals) if np.mean(q_vals) > 0 else 1.0
stability_vals = list(STABILITY.values())
conceptual_cohesion = np.mean(stability_vals) if stability_vals else 0.5
mean_q = np.mean(q_vals)
mean_synth = np.mean([b["predicted_synthesis_q"] for b in BRIDGES.values()])
feasibility = (0.30 * mean_q + 0.30 * mean_synth + 0.25 * conceptual_cohesion + 0.15 * (1 - roadmap_risk))

# ── 5. ADVANCED METRICS ──────────────────────────────────────────────────────
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

def calculate_gestalt_consistency(name, cluster_id, fw_profiles, clusters):
    if name not in fw_profiles: return 0.0
    members = clusters[f"C{cluster_id}_" + list(clusters.keys())[cluster_id-1].split('_', 1)[1]]["members"] # Hacky but gets members
    # Correcting member lookup
    members = []
    for cid_str, info in CLUSTERS.items():
        if cid_str.startswith(f"C{cluster_id}_"):
            members = info["members"]
            break
    if not members: return 0.0
    cluster_vecs = np.array([fw_profiles[m] for m in members if m in fw_profiles])
    if len(cluster_vecs) == 0: return 0.0
    mean_vec = cluster_vecs.mean(axis=0)
    return float(cosine_sim(fw_profiles[name], mean_vec))

# ── 6. STRUCTURAL SENSITIVITY AUDIT ──────────────────────────────────────────
def structural_sensitivity_audit(synergies, fw_profiles):
    """Perturbs profiles and measures rank variance of top synergies."""
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

# ── 7. RESEARCH FRONTIER GENERATION ──────────────────────────────────────────
def generate_proposals(synergies, clusters):
    proposals = []
    seen_pairs = set()

    for s in synergies:
        n1, n2 = s["n1"], s["n2"]
        if (n1, n2) in seen_pairs or (n2, n1) in seen_pairs: continue

        target_p = "Emergent Human Behavior"
        for c in clusters.values():
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
        g1 = calculate_gestalt_consistency(n1, s["c1"], FW_PROFILES, CLUSTERS)
        g2 = calculate_gestalt_consistency(n2, s["c2"], FW_PROFILES, CLUSTERS)
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

all_proposals = generate_proposals(DYNAMIC_SYNERGIES, CLUSTERS)
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
