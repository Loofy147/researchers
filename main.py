from src.math_unification.analysis.framework import run_framework_analysis
from src.math_unification.analysis.qscore import run_qscore_analysis
from src.math_unification.synthesis.report import generate_report
from src.math_unification.synthesis.papers import generate_research_papers

def main():
    print("--- Starting Mathematical Unification Pipeline (v5.3) ---")

    print("\n[1/4] Running Framework Analysis...")
    run_framework_analysis()

    print("\n[2/4] Running Q-Score & Sensitivity Analysis...")
    run_qscore_analysis()

    print("\n[3/4] Generating Research Paper Abstracts...")
    generate_research_papers()

    print("\n[4/4] Generating Synthesis Report...")
    generate_report()

    print("\n--- Pipeline Execution Complete ---")
    print("Results available in synthesis_report.md, adversarial_analysis.md, and research_papers.json.")

if __name__ == "__main__":
    main()
