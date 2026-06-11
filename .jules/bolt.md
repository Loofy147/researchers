## 2025-05-15 - [Pre-calculating NumPy arrays for repeated metrics]
**Learning:** In heavy analysis pipelines where the same profiles are used in nested loops (e.g., cosine similarity between frameworks and phenomena), pre-converting lists to NumPy arrays and caching mean vectors for clusters provides a measurable speedup (~50% in this case) without sacrificing readability.
**Action:** Always identify static data being converted to NumPy arrays inside loops and move the conversion outside the loop.

## 2025-05-15 - [Vectorizing Sensitivity Audits]
**Learning:** Sensitivity audits involving perturbations and re-ranking are prime candidates for NumPy vectorization. By converting profile dictionaries to matrices and using broadcasted operations for noise and similarity, I achieved a 5x speedup for that specific component.
**Action:** Use NumPy index arrays and sum-reduction for batch similarity calculations instead of iterating over synergy lists.

## 2025-05-15 - [Batch Vectorization of Metrics]
**Learning:** Moving from scalar-based NumPy calls (inside a loop) to true batch vectorization (passing the entire dataset to NumPy) provides another 2x speedup. Normalizing vectors once (e.g., ) and then using  for batch cosine similarity is extremely efficient.
**Action:** When calculating metrics for many pairs, use index arrays to select rows from a normalized matrix and perform element-wise multiplication followed by sum-reduction.

## 2025-05-15 - [Batch Vectorization of Metrics]
**Learning:** Moving from scalar-based NumPy calls (inside a loop) to true batch vectorization (passing the entire dataset to NumPy) provides another 2x speedup. Normalizing vectors once (e.g., FW_Xn) and then using np.sum(A * B, axis=1) for batch cosine similarity is extremely efficient.
**Action:** When calculating metrics for many pairs, use index arrays to select rows from a normalized matrix and perform element-wise multiplication followed by sum-reduction.
