"""
Q-Score Analysis for each cluster + integration strategy computation
"""
import numpy as np
import json

# Cluster assignments from prior analysis
CLUSTERS = {
    "C1_Symbolic_Structure": {
        "members": ["Category Theory", "Formal Grammars", "Algebraic Linguistics", "Categorical Quantum Mechanics"],
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
        "members": ["Game Theory","Prospect Theory","Bayesian Inference","Social Choice Theory","Stochastic Processes","Measure-Theoretic Prob."],
        "dominant_axes": ["measure_theory", "stochastic_processes"],
        "human_domain": "Decision, Rationality, Risk",
        "scores": {"Grounding": 0.88, "Certainty": 0.84, "Structure": 0.82, "Applicability": 0.92, "Coherence": 0.79, "Generativity": 0.85, "Presentation": 0.82, "Temporal": 0.86},
        "phenomena": ["The lipstick effect", "Influencer commodification", "Decision fatigue", "The Barnum effect", "The mere exposure effect", "Pascal's wager", "Ethical egoism", "The veil of ignorance", "Soft authoritarianism", "Geopolitical strategy", "Proxy wars", "Hyperinflation", "Venture debt", "Short selling", "Monopoly power", "Recession indicators", "Leveraged buyouts", "Speculative markets", "Wealth inequality"]
    },
    "C4_Collective_Dynamics": {
        "members": ["Neural Field Theory","Integrated Info Theory","Global Workspace Theory","Dynamical Systems Psych","Mean Field Theory","Evolutionary Game Theory","Network Science","Agent-Based Modeling","Renormalization Group", "Geometric Deep Learning", "Statistical Physics"],
        "dominant_axes": ["dynamical_systems", "statistical_mechanics"],
        "human_domain": "Consciousness, Social Emergence, Brain Dynamics",
        "scores": {"Grounding": 0.79, "Certainty": 0.70, "Structure": 0.76, "Applicability": 0.78, "Coherence": 0.72, "Generativity": 0.88, "Presentation": 0.68, "Temporal": 0.80},
        "phenomena": ["Neurodivergence", "Oxytocin and bonding", "Neural pathways", "Data monopolies", "Digital immortality", "Beauty standards", "Quiet luxury", "Trend forecasting", "Personal branding", "Pretty privilege", "Parasocial relationships", "Stan culture", "Rebrand culture", "Internet fame cycles", "Cancel culture", "Reality TV psychology", "The bystander effect", "Love bombing", "Trauma bonding", "Panpsychism", "Neocolonialism", "Populism", "Nationalism", "The military-industrial complex", "Venture scaling", "Third culture kids", "Cultural assimilation", "Digital subcultures", "Hyper consumerism", "Hustle culture", "Modern loneliness", "Luxury signalling", "Inductive biases"]
    },
    "C5_Geometric_Optimization": {
        "members": ["Variational Principles","Gradient Flow Theory","Riemannian Geometry","Geometric Mechanics","Symplectic Geometry"],
        "dominant_axes": ["geometry", "optimization"],
        "human_domain": "Motor Control, Learning Geometry, Physical Embodiment",
        "scores": {"Grounding": 0.76, "Certainty": 0.80, "Structure": 0.92, "Applicability": 0.67, "Coherence": 0.87, "Generativity": 0.79, "Presentation": 0.65, "Temporal": 0.75},
        "phenomena": ["Phantom limb syndrome", "Symmetry constraints"]
    },
    "C6_Agency_Control": {
        "members": ["Optimal Control","Reinforcement Learning","Free Energy Principle","Predictive Coding", "Computational Psychiatry"],
        "dominant_axes": ["optimization", "control_theory"],
        "human_domain": "Active Inference, Goal-Directed Behavior",
        "scores": {"Grounding": 0.85, "Certainty": 0.81, "Structure": 0.86, "Applicability": 0.88, "Coherence": 0.84, "Generativity": 0.90, "Presentation": 0.78, "Temporal": 0.84},
        "phenomena": ["Dopamine detoxing", "The placebo effect", "Cognitive overload", "Neural interfaces", "Autonomous vehicles", "Emotional permanence", "Repression", "Solipsism", "Virtue ethics", "Simulation theory", "Mental health diagnostics"]
    }
}

WEIGHTS = {'Grounding':0.23,'Certainty':0.15,'Structure':0.18,'Applicability':0.16, 'Coherence':0.12,'Generativity':0.08,'Presentation':0.05,'Temporal':0.03}

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

q_results = {}
for cid, info in CLUSTERS.items():
    q_results[cid] = {
        "q_score": q_score(info["scores"]),
        "human_domain": info["human_domain"],
        "members": info["members"],
        "dominant_axes": info["dominant_axes"],
        "phenomena": info["phenomena"]
    }

mean_q = np.mean([v["q_score"] for v in q_results.values()])
mean_synth = np.mean([b["predicted_synthesis_q"] for b in BRIDGES.values()])
feasibility = 0.35 * mean_q + 0.30 * mean_synth + 0.20 * 1.0 + 0.15 * 1.0

with open("qscore_results.json", "w") as f:
    json.dump({
        "cluster_results": q_results,
        "bridges": BRIDGES,
        "metrics": {
            "mean_cluster_q": mean_q,
            "mean_bridge_q": mean_synth,
            "feasibility": feasibility
        }
    }, f, indent=2)

print("Q-score analysis complete. Results saved to qscore_results.json.")
