import numpy as np
from ..data import AXES

def calculate_research_transactions(embeddings, profiles, names, q_map):
    """
    Generates 'Research Transactions' based on coordinate distances and Q-score differentials.
    """
    transactions = []

    # Pre-calculate distances in embedding space
    emb_array = np.array([embeddings[n] for n in names])
    # Coordinate proximity check
    dist_matrix = np.sqrt(np.sum((emb_array[:, np.newaxis, :] - emb_array[np.newaxis, :, :])**2, axis=2))

    for i, n1 in enumerate(names):
        for j, n2 in enumerate(names):
            if i == j: continue

            dist = dist_matrix[i, j]
            if dist < 0.3: # Proximity threshold for transaction
                q1 = q_map.get(n1, 0.5)
                q2 = q_map.get(n2, 0.5)

                # Flow from source to target if source has higher utility or specific assets
                if q1 > q2:
                    improvement_potential = (q1 - q2) / (dist + 0.1)

                    v1 = np.array(profiles[n1])
                    v2 = np.array(profiles[n2])

                    # Assets are axes where source can improve target
                    asset_indices = np.where((v1 > 0.7) & (v1 > v2 + 0.3))[0]
                    assets = [AXES[idx] for idx in asset_indices]

                    if assets:
                        transactions.append({
                            "source": n1,
                            "target": n2,
                            "improvement_potential": float(improvement_potential),
                            "transacted_assets": assets,
                            "distance": float(dist),
                            "transaction_id": f"TX-{n1[:3].upper()}-{n2[:3].upper()}"
                        })

    # Sort by potential and deduplicate
    transactions.sort(key=lambda x: -x["improvement_potential"])
    unique_tx = []
    seen = set()
    for tx in transactions:
        pair = (tx["source"], tx["target"])
        if pair not in seen:
            unique_tx.append(tx)
            seen.add(pair)

    return unique_tx[:12] # Return top 12 transactions
