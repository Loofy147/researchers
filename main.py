import subprocess
import sys

def run_script(name):
    print(f"--- Running {name} ---")
    result = subprocess.run(["python3", name], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error in {name}:")
        print(result.stderr)
        sys.exit(1)
    print(result.stdout)

def main():
    scripts = ["framework_analysis.py", "qscore_analysis.py", "synthesis_doc.py"]
    for script in scripts:
        run_script(script)
    print("--- Pipeline Execution Complete ---")
    print("Final report generated: synthesis_report.md")

if __name__ == "__main__":
    main()
