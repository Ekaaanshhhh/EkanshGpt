import requests

docs = [
    {
        "filename": "ekansh_resume.txt",
        "old_path": "downloads/ekansh_resume.pdf",
        "category": "resume",
        "name": "Ekansh Resume"
    },
    {
        "filename": "medisaar_summary.txt",
        "old_path": "downloads/medisaar_summary.pdf",
        "category": "project",
        "name": "MediSaar Summary"
    },
    {
        "filename": "reelops_summary.txt",
        "old_path": "downloads/reelops_summary.pdf",
        "category": "project",
        "name": "ReelOps Summary"
    },
    {
        "filename": "personal_kb.txt",
        "old_path": "downloads/personal_kb.pdf",
        "category": "blog",
        "name": "Personal Knowledge Base"
    }
]

# We will also ingest the user's summary.md directly
docs.append({
    "filename": "summary.md",
    "old_path": "/Users/ekanshsatsangi/Desktop/untitled folder/summary.md",
    "category": "resume",
    "name": "Comprehensive Knowledge Base Summary"
})

for doc in docs:
    print(f"Uploading {doc['name']} to backend...")
    try:
        with open(doc['old_path'], 'rb') as f:
            # We pass the new filename to the API
            files = {'file': (doc['filename'], f, 'text/plain')}
            data = {
                'category': doc['category'],
                'document_name': doc['name']
            }
            response = requests.post("http://localhost:8000/api/ingest/upload", files=files, data=data)
            
            if response.status_code == 200:
                print(f"Success: {response.json()}")
            else:
                print(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        print(f"Failed: {e}")
    print("-" * 40)
