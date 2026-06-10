"""
Q-Score Analysis for each cluster + integration strategy computation
"""
import numpy as np

# Cluster assignments from prior analysis
CLUSTERS = {
    "C1_Symbolic_Structure": {
        "members": ["Category Theory", "Formal Grammars", "Algebraic Linguistics"],
        "dominant_axes": ["logic_formal", "algebra_structure"],
        "human_domain": "Language, Logic, Cultural Form",
        "scores": {
            "Grounding":      0.72,   # logic is solid but empirical link to cognition weak
            "Certainty":      0.85,   # formal proofs, decidability results
            "Structure":      0.95,   # highest structural clarity of all clusters
            "Applicability":  0.60,   # NLP is growing; sociolinguistics partial
            "Coherence":      0.90,   # internally unified
            "Generativity":   0.78,   # generates novel grammatical/algebraic models
            "Presentation":   0.70,
            "Temporal":       0.88,
        }
    },
    "C2_Representational_Geometry": {
        "members": ["Information Geometry","Quantum Cognition","Topological Data Anal.",
                    "Fourier/Wavelet Anal.","Compressed Sensing"],
        "dominant_axes": ["linear_algebra", "geometry"],
        "human_domain": "Representation, Perception, Signal",
        "scores": {
            "Grounding":      0.82,   # strong in neural imaging, signal analysis
            "Certainty":      0.78,
            "Structure":      0.88,
            "Applicability":  0.85,   # fMRI, neuroscience, psychophysics
            "Coherence":      0.80,
            "Generativity":   0.83,
            "Presentation":   0.75,
            "Temporal":       0.82,
        }
    },
    "C3_Probabilistic_Choice": {
        "members": ["Game Theory","Prospect Theory","Bayesian Inference",
                    "Social Choice Theory","Stochastic Processes","Measure-Theoretic Prob."],
        "dominant_axes": ["measure_theory", "stochastic_processes"],
        "human_domain": "Decision, Rationality, Risk",
        "scores": {
            "Grounding":      0.88,   # behavioural econ, psych experiments
            "Certainty":      0.84,
            "Structure":      0.82,
            "Applicability":  0.92,   # policy, econ, clinical decision
            "Coherence":      0.79,
            "Generativity":   0.85,
            "Presentation":   0.82,
            "Temporal":       0.86,
        }
    },
    "C4_Collective_Dynamics": {
        "members": ["Neural Field Theory","Integrated Info Theory","Global Workspace Theory",
                    "Dynamical Systems Psych","Mean Field Theory","Evolutionary Game Theory",
                    "Network Science","Agent-Based Modeling","Renormalization Group"],
        "dominant_axes": ["dynamical_systems", "statistical_mechanics"],
        "human_domain": "Consciousness, Social Emergence, Brain Dynamics",
        "scores": {
            "Grounding":      0.79,   # broad but sometimes loose
            "Certainty":      0.70,   # IIT contested; GWT empirical but partial
            "Structure":      0.76,
            "Applicability":  0.78,   # brain disorder models, epidemiology
            "Coherence":      0.72,   # heterogeneous cluster
            "Generativity":   0.88,   # richest in novel predictions
            "Presentation":   0.68,
            "Temporal":       0.80,
        }
    },
    "C5_Geometric_Optimization": {
        "members": ["Variational Principles","Gradient Flow Theory","Riemannian Geometry",
                    "Geometric Mechanics","Symplectic Geometry"],
        "dominant_axes": ["geometry", "optimization"],
        "human_domain": "Motor Control, Learning Geometry, Physical Embodiment",
        "scores": {
            "Grounding":      0.76,   # motor control well-grounded; cognition partial
            "Certainty":      0.80,
            "Structure":      0.92,   # differential geometry is maximally precise
            "Applicability":  0.67,   # robotics strong; cognitive science partial
            "Coherence":      0.87,
            "Generativity":   0.79,
            "Presentation":   0.65,
            "Temporal":       0.75,
        }
    },
    "C6_Agency_Control": {
        "members": ["Optimal Control","Reinforcement Learning","Free Energy Principle","Predictive Coding"],
        "dominant_axes": ["optimization", "control_theory"],
        "human_domain": "Active Inference, Goal-Directed Behavior",
        "scores": {
            "Grounding":      0.85,   # RL in neuroscience; FEP growing
            "Certainty":      0.81,
            "Structure":      0.86,
            "Applicability":  0.88,   # AI, robotics, psychiatry
            "Coherence":      0.84,
            "Generativity":   0.90,   # FEP/PC generating fast new predictions
            "Presentation":   0.78,
            "Temporal":       0.84,
        }
    }
}

WEIGHTS = {'Grounding':0.18,'Certainty':0.20,'Structure':0.18,'Applicability':0.16,
           'Coherence':0.12,'Generativity':0.08,'Presentation':0.05,'Temporal':0.03}

def q_score(scores):
    return sum(WEIGHTS[k] * v for k, v in scores.items())

print("=== CLUSTER Q-SCORES ===")
results = {}
for cid, info in CLUSTERS.items():
    q = q_score(info["scores"])
    bottleneck = min(info["scores"], key=lambda k: info["scores"][k] * WEIGHTS[k])
    strength   = max(info["scores"], key=lambda k: info["scores"][k] * WEIGHTS[k])
    results[cid] = q
    print(f"\n{cid}")
    print(f"  Q-score      : {q:.3f}")
    print(f"  Domain       : {info['human_domain']}")
    print(f"  Bottleneck   : {bottleneck}  ({info['scores'][bottleneck]:.2f})")
    print(f"  Strength     : {strength}  ({info['scores'][strength]:.2f})")
    print(f"  Members      : {len(info['members'])}")

# ── BRIDGE CONCEPT INTEGRATION MATRIX ────────────────────────────────────
print("\n\n=== BRIDGE CONCEPT INTEGRATION MATRIX ===")
bridges = {
    "Free Energy Principle\n(C6↔C4, C6↔C5)": {
        "connects": ["C6_Agency_Control","C4_Collective_Dynamics","C5_Geometric_Optimization"],
        "mechanism": "Unifies variational inference (C6), nonlinear dynamics (C4), and Riemannian gradient flows (C5) under a single Lagrangian: F = KL[Q||P] – log P(o|m). Motor control, neural dynamics, and belief updating become one.",
        "predicted_synthesis_q": 0.897,
        "key_equation": "dμ/dt = -∂F/∂μ  [gradient descent on variational free energy]"
    },
    "Topological Data Analysis\n(C2↔C1, C2↔C4)": {
        "connects": ["C2_Representational_Geometry","C1_Symbolic_Structure","C4_Collective_Dynamics"],
        "mechanism": "Persistent homology (C2) reads topological invariants from neural data (C4) and maps them to grammatical/categorical structure (C1). Bridging between signal representation and symbolic cognition.",
        "predicted_synthesis_q": 0.873,
        "key_equation": "H_k(X) — k-th homology group as structural fingerprint across scales"
    },
    "Stochastic Optimal Control\n(C3↔C6, C3↔C5)": {
        "connects": ["C3_Probabilistic_Choice","C6_Agency_Control","C5_Geometric_Optimization"],
        "mechanism": "Hamilton-Jacobi-Bellman equation on statistical manifolds (C5) yields rational choice under uncertainty (C3) with neural implementation via optimal control (C6). Unifies prospect theory and motor control.",
        "predicted_synthesis_q": 0.885,
        "key_equation": "∂V/∂t + H(x, ∇V, t) = 0  on Riemannian (M, g)"
    },
    "Categorical Probability\n(C1↔C3)": {
        "connects": ["C1_Symbolic_Structure","C3_Probabilistic_Choice"],
        "mechanism": "Kleisli categories for probability monads (C1) give compositional semantics to Bayesian updating (C3). Language, logic, and probabilistic inference become morphisms in one category.",
        "predicted_synthesis_q": 0.852,
        "key_equation": "P : C → Kleisli(Dist)  [probability as functor]"
    },
    "Renormalization / Scale Symmetry\n(C4↔C5↔C2)": {
        "connects": ["C4_Collective_Dynamics","C5_Geometric_Optimization","C2_Representational_Geometry"],
        "mechanism": "Fixed points of renormalization group flow (C4) correspond to critical brain states; geometric flow on representation manifolds (C5) scales information compression (C2). Connects collective criticality, learning geometry, and perception.",
        "predicted_synthesis_q": 0.868,
        "key_equation": "dg_μν/dt = -2 R_μν  [Ricci flow as RG on geometry]"
    }
}

for bname, info in bridges.items():
    print(f"\n★ {bname}")
    print(f"  Connects  : {' + '.join(info['connects'])}")
    print(f"  Mechanism : {info['mechanism'][:130]}...")
    print(f"  Key eq.   : {info['key_equation']}")
    print(f"  Synth. Q  : {info['predicted_synthesis_q']:.3f}")

# ── UNIFIED FRAMEWORK CANDIDATE SCORE ────────────────────────────────────
print("\n\n=== UNIFIED FRAMEWORK FEASIBILITY ===")
cluster_qs = list(results.values())
mean_q = np.mean(cluster_qs)
coverage = 1.0  # 6 clusters span all major domains
bridge_count = len(bridges)
synth_qs = [b["predicted_synthesis_q"] for b in bridges.values()]
mean_synth = np.mean(synth_qs)

feasibility = 0.35 * mean_q + 0.30 * mean_synth + 0.20 * min(coverage,1) + 0.15 * min(bridge_count/5, 1)
print(f"  Mean cluster Q          : {mean_q:.3f}")
print(f"  Mean bridge synthesis Q : {mean_synth:.3f}")
print(f"  Domain coverage         : {coverage:.1f}")
print(f"  Active bridge count     : {bridge_count}")
print(f"  UNIFICATION FEASIBILITY : {feasibility:.3f}")
print(f"  Verdict: {'VIABLE — pursue staged integration' if feasibility > 0.80 else 'Partial — focus on highest-Q clusters'}")
