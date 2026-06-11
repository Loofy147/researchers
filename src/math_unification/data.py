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

MACRO_AXES = {
    "Symbolic/Formal": ["algebra_structure", "logic_formal", "topology"],
    "Statistical/Prob": ["stochastic_processes", "information_theory", "measure_theory", "statistical_mechanics"],
    "Cybernetic/Control": ["optimization", "dynamical_systems", "control_theory", "game_theory", "signal_processing"],
    "Structural/Geometric": ["geometry", "network_graph", "linear_algebra"]
}
