## 2025-05-15 - [Pre-calculating NumPy arrays for repeated metrics]
**Learning:** In heavy analysis pipelines where the same profiles are used in nested loops (e.g., cosine similarity between frameworks and phenomena), pre-converting lists to NumPy arrays and caching mean vectors for clusters provides a measurable speedup (~50% in this case) without sacrificing readability.
**Action:** Always identify static data being converted to NumPy arrays inside loops and move the conversion outside the loop.
