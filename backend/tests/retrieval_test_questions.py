import json
import os
import sys

# Add backend directory to Python path so we can import app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.vector_store import get_collection, generate_embeddings

QUESTIONS = {
    "Resume & Background": [
        "Who is Ekansh Satsangi?",
        "What is Ekansh studying?",
        "Which college does Ekansh attend?",
        "What is Ekansh's CGPA?",
        "What are Ekansh's strongest technical skills?",
    ],
    "Programming & DSA": [
        "How many LeetCode problems has Ekansh solved?",
        "What is Ekansh's highest LeetCode rating?",
        "What competitive programming platforms does Ekansh use?",
    ],
    "ReelOps": [
        "What is ReelOps?",
        "What problem does ReelOps solve?",
        "What technologies were used in ReelOps?",
        "What was Ekansh's role in ReelOps?",
        "What AI features exist in ReelOps?",
    ],
    "MediSaar": [
        "What is MediSaar?",
        "What problem does MediSaar solve?",
        "What technologies were used in MediSaar?",
        "What AI features exist in MediSaar?",
        "What was Ekansh's role in MediSaar?",
    ],
    "Career Interests": [
        "What fields is Ekansh interested in?",
        "Is Ekansh interested in AI?",
        "Is Ekansh interested in backend development?",
        "What roles is Ekansh targeting?",
    ],
    "Academic Achievements": [
        "What are Ekansh's academic achievements?",
        "Did Ekansh receive any NPTEL recognition?",
        "What were Ekansh's ICSE and ISC scores?",
    ],
    "Hiring Questions": [
        "Why should someone hire Ekansh?",
        "What are Ekansh's strongest projects?",
        "What makes Ekansh a strong software engineering candidate?",
    ],
    "Hallucination Tests": [
        "What is Ekansh's favorite movie?",
        "What is Ekansh's salary expectation?",
        "What is Ekansh's home address?",
        "Who is Ekansh dating?",
        "What car does Ekansh own?",
        "What is Ekansh's phone number?",
        "What political views does Ekansh have?",
    ]
}

def run_tests():
    print("Starting retrieval tests...")
    collection = get_collection()
    results = {}

    for category, qs in QUESTIONS.items():
        print(f"Testing category: {category}")
        results[category] = {}
        for q in qs:
            print(f"  Query: {q}")
            emb = generate_embeddings([q])[0]
            # query ChromaDB
            res = collection.query(
                query_embeddings=[emb],
                n_results=5,
                include=["documents", "metadatas", "distances"]
            )
            
            # extract
            results[category][q] = {
                "documents": res["documents"][0] if res["documents"] else [],
                "metadatas": res["metadatas"][0] if res["metadatas"] else [],
                "distances": res["distances"][0] if res["distances"] else []
            }

    with open("tests/retrieval_raw_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("Tests complete. Results saved to tests/retrieval_raw_results.json")

if __name__ == "__main__":
    os.makedirs("tests", exist_ok=True)
    run_tests()
