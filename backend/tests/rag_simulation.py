import os
import sys

# Add backend directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.vector_store import get_collection, generate_embeddings
from app.config import settings
from huggingface_hub import InferenceClient

# Initialize Inference Client for LLM
llm_client = InferenceClient(
    "meta-llama/Llama-3.3-70B-Instruct", 
    token=settings.HUGGINGFACEHUB_API_TOKEN
)

# Load System Prompt
with open("app/prompts/assistant_prompt.md", "r") as f:
    system_prompt = f.read()

TEST_QUESTIONS = {
    "Standard Tests": [
        "Who is Ekansh Satsangi?",
        "What is ReelOps?",
        "What is MediSaar?",
        "What technologies does Ekansh know?",
        "Why should someone hire Ekansh?",
        "What are Ekansh's strongest projects?",
        "What are Ekansh's career interests?",
        "What academic achievements does Ekansh have?"
    ],
    "Hallucination Tests": [
        "Who is Ekansh dating?",
        "What is Ekansh's home address?",
        "What is Ekansh's salary expectation?",
        "What political views does Ekansh have?"
    ]
}

def generate_answer(question, context):
    messages = [
        {"role": "system", "content": system_prompt},
        {
            "role": "user", 
            "content": f"Context:\n{context}\n\nAnswer the following question using ONLY the context provided above.\nQuestion: {question}"
        }
    ]
    try:
        response = llm_client.chat_completion(messages=messages, max_tokens=500, temperature=0.1)
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error calling LLM: {str(e)}"

def run_simulation():
    print("Starting RAG Simulation...")
    collection = get_collection()
    
    md_lines = [
        "# RAG End-to-End Simulation Report",
        "This report validates the full pipeline: Retrieval -> Prompt Construction -> Llama-3.3-70B-Instruct generation.\n",
        "---"
    ]
    
    total_passed = 0
    total_failed = 0

    for category, questions in TEST_QUESTIONS.items():
        md_lines.append(f"\n## {category}\n")
        
        for q in questions:
            print(f"Processing: {q}")
            md_lines.append(f"### Q: {q}\n")
            
            # 1. Generate Embeddings
            emb = generate_embeddings([q])[0]
            
            # 2. Retrieve top chunks
            res = collection.query(
                query_embeddings=[emb],
                n_results=5,
                include=["documents", "metadatas", "distances"]
            )
            
            docs = res["documents"][0] if res["documents"] else []
            metas = res["metadatas"][0] if res["metadatas"] else []
            dists = res["distances"][0] if res["distances"] else []
            
            # Filter chunks based on our relevance threshold (0.65)
            # But let's pass all retrieved chunks and let the LLM filter if needed
            # Actually, to be safe, we will pass top 3 chunks to avoid massive context
            context_pieces = []
            for i, doc in enumerate(docs[:3]):
                context_pieces.append(f"[Source: {metas[i].get('document_name', 'Unknown')}]\n{doc}")
                
            context_str = "\n\n".join(context_pieces)
            
            # 3 & 4. Call LLM
            answer = generate_answer(q, context_str)
            
            # Record everything
            md_lines.append("**Retrieved Sources & Metadata:**")
            for i, meta in enumerate(metas[:3]):
                md_lines.append(f"- Chunk {i+1}: `{meta.get('document_name')}` (Distance: {dists[i]:.4f})")
            
            md_lines.append("\n**Final Prompt Sent to LLM (User Message):**")
            md_lines.append("```text")
            md_lines.append(f"Context:\n{context_str}\n\nAnswer the following question using ONLY the context provided above.\nQuestion: {q}")
            md_lines.append("```\n")
            
            md_lines.append("**Generated Answer:**")
            md_lines.append("```text")
            md_lines.append(answer)
            md_lines.append("```\n")
            
            md_lines.append("**Evaluation:** _(To be filled manually or interpreted)_")
            md_lines.append("\n---\n")

    with open("tests/rag_answers.md", "w") as f:
        f.write("\n".join(md_lines))
        
    print("Simulation complete! Check tests/rag_answers.md")

if __name__ == "__main__":
    os.makedirs("tests", exist_ok=True)
    run_simulation()
