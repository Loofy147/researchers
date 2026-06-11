import json

def generate_research_papers():
    try:
        with open("qscore_results.json", "r") as f:
            qs = json.load(f)
        frontiers = qs.get("research_frontiers", [])[:3]
    except Exception as e:
        print(f"Error loading qscore results: {e}")
        return

    papers = []
    for f in frontiers:
        abstract = {
            "title": f["title"],
            "background": f"Current models of {f['target_phenomenon']} lack a unified formal foundation. This paper proposes a synthesis between {f['title'].split(': ')[1]}.",
            "methodology": f"Utilizing a {f['validation_audit']} approach, we construct a morphism between the respective conceptual manifolds, validated by an Anchor Score of {f['anchor_score']:.3f}.",
            "hypothesis": f["core_hypothesis"],
            "impact": f"This unification provides a rigorous framework for understanding {f['target_phenomenon']}, potentially bridging the gap between symbolic and statistical models."
        }
        papers.append(abstract)

    with open("research_papers.json", "w") as f:
        json.dump(papers, f, indent=2)
    print("Research papers generated: research_papers.json")

if __name__ == "__main__":
    generate_research_papers()
