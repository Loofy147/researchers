import time
from src.math_unification.analysis.framework import run_framework_analysis

start = time.time()
for _ in range(10):
    run_framework_analysis()
end = time.time()
print(f"Average time over 10 runs: {(end - start)/10:.4f}s")
