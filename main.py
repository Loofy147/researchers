from src.math_unification.analysis.framework import run_framework_analysis
from src.math_unification.analysis.qscore import run_qscore_analysis
from src.math_unification.synthesis.report import generate_report

def main():
    print("--- Starting Mathematical Unification Pipeline (v5.3) ---")

    print("\n[1/3] Running Framework Analysis...")
    run_framework_analysis()

    print("\n[2/3] Running Q-Score & Sensitivity Analysis...")
    run_qscore_analysis()

    print("\n[3/3] Generating Synthesis Report...")
    generate_report()

    print("\n--- Pipeline Execution Complete ---")
    print("Results available in synthesis_report.md and adversarial_analysis.md.")

if __name__ == "__main__":
    main()
