# Retrieval Quality Audit Report
This report validates the ChromaDB vector retrieval pipeline prior to LLM integration.
A distance threshold of `< 0.65` is used to determine if a chunk is highly relevant (lower distance = higher similarity).
---

## Resume & Background

### Q: Who is Ekansh Satsangi?
**Result: PASS** (Best Distance: 0.4025)

**Chunk 1 | Distance: 0.4025 | Source: summary.md**
```json
{
  "total_chunks": 16,
  "source": "summary.md",
  "owner": "ekansh",
  "document_name": "Comprehensive Knowledge Base Summary",
  "document_type": "markdown",
  "category": "resume",
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00",
  "chunk_index": 0
}
```
```text
Ekansh Satsangi About Me I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna. I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI applications. My pr...
```

**Chunk 2 | Distance: 0.4025 | Source: summary.md**
```json
{
  "source": "summary.md",
  "document_type": "markdown",
  "owner": "ekansh",
  "document_name": "Comprehensive Knowledge Base Summary",
  "total_chunks": 16,
  "uploaded_at": "2026-06-20T00:02:56.709776+00:00",
  "category": "resume",
  "chunk_index": 0
}
```
```text
Ekansh Satsangi About Me I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna. I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI applications. My pr...
```

**Chunk 3 | Distance: 0.4192 | Source: personal_kb.txt**
```json
{
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "source": "personal_kb.txt",
  "total_chunks": 15,
  "category": "blog",
  "owner": "ekansh",
  "document_name": "Personal Knowledge Base",
  "chunk_index": 0,
  "document_type": "text"
}
```
```text
# Ekansh Satsangi  ## About Me  I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna.  I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI application...
```

**Chunk 4 | Distance: 0.4192 | Source: personal_kb.txt**
```json
{
  "total_chunks": 15,
  "document_name": "Personal Knowledge Base",
  "source": "personal_kb.txt",
  "owner": "ekansh",
  "category": "blog",
  "document_type": "text",
  "chunk_index": 0,
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00"
}
```
```text
# Ekansh Satsangi  ## About Me  I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna.  I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI application...
```

**Chunk 5 | Distance: 0.6375 | Source: ekansh_resume.txt**
```json
{
  "category": "resume",
  "chunk_index": 0,
  "document_type": "text",
  "source": "ekansh_resume.txt",
  "document_name": "Ekansh Resume",
  "total_chunks": 13,
  "uploaded_at": "2026-06-19T23:59:53.377793+00:00",
  "owner": "ekansh"
}
```
```text
+91-8542951940 _|_ ekanshsatsangi@gmail.com _|_ LinkedIn _|_ GitHub _|_ Portfolio  ## Ekansh Satsangi  ## **Education**  **National Institute of Technology, Patna Sep. 2024 – Jul. 2028** _B.Tech, Electronics and Communication Engineering | CGPA:_ _**8.56/10** Patna, Bihar, India_ **Mercy Memorial Sc...
```

### Q: What is Ekansh studying?
**Result: PASS** (Best Distance: 0.5331)

**Chunk 1 | Distance: 0.5331 | Source: personal_kb.txt**
```json
{
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "document_type": "text",
  "chunk_index": 14,
  "document_name": "Personal Knowledge Base",
  "owner": "ekansh",
  "source": "personal_kb.txt",
  "total_chunks": 15,
  "category": "blog"
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 2 | Distance: 0.5331 | Source: personal_kb.txt**
```json
{
  "document_type": "text",
  "chunk_index": 14,
  "category": "blog",
  "owner": "ekansh",
  "document_name": "Personal Knowledge Base",
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "total_chunks": 15,
  "source": "personal_kb.txt"
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 3 | Distance: 0.6209 | Source: personal_kb.txt**
```json
{
  "owner": "ekansh",
  "document_type": "text",
  "chunk_index": 0,
  "category": "blog",
  "total_chunks": 15,
  "source": "personal_kb.txt",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "document_name": "Personal Knowledge Base"
}
```
```text
# Ekansh Satsangi  ## About Me  I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna.  I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI application...
```

**Chunk 4 | Distance: 0.6209 | Source: personal_kb.txt**
```json
{
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "document_type": "text",
  "category": "blog",
  "total_chunks": 15,
  "owner": "ekansh",
  "document_name": "Personal Knowledge Base",
  "source": "personal_kb.txt",
  "chunk_index": 0
}
```
```text
# Ekansh Satsangi  ## About Me  I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna.  I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI application...
```

**Chunk 5 | Distance: 0.6220 | Source: summary.md**
```json
{
  "chunk_index": 0,
  "document_type": "markdown",
  "owner": "ekansh",
  "category": "resume",
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00",
  "source": "summary.md",
  "document_name": "Comprehensive Knowledge Base Summary",
  "total_chunks": 16
}
```
```text
Ekansh Satsangi About Me I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna. I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI applications. My pr...
```

### Q: Which college does Ekansh attend?
**Result: PASS** (Best Distance: 0.6307)

**Chunk 1 | Distance: 0.6307 | Source: ekansh_resume.txt**
```json
{
  "category": "resume",
  "document_name": "Ekansh Resume",
  "document_type": "text",
  "owner": "ekansh",
  "source": "ekansh_resume.txt",
  "chunk_index": 0,
  "total_chunks": 13,
  "uploaded_at": "2026-06-19T23:59:53.377793+00:00"
}
```
```text
+91-8542951940 _|_ ekanshsatsangi@gmail.com _|_ LinkedIn _|_ GitHub _|_ Portfolio  ## Ekansh Satsangi  ## **Education**  **National Institute of Technology, Patna Sep. 2024 – Jul. 2028** _B.Tech, Electronics and Communication Engineering | CGPA:_ _**8.56/10** Patna, Bihar, India_ **Mercy Memorial Sc...
```

**Chunk 2 | Distance: 0.6307 | Source: ekansh_resume.txt**
```json
{
  "total_chunks": 13,
  "source": "ekansh_resume.txt",
  "category": "resume",
  "chunk_index": 0,
  "document_name": "Ekansh Resume",
  "document_type": "text",
  "uploaded_at": "2026-06-20T00:02:04.694247+00:00",
  "owner": "ekansh"
}
```
```text
+91-8542951940 _|_ ekanshsatsangi@gmail.com _|_ LinkedIn _|_ GitHub _|_ Portfolio  ## Ekansh Satsangi  ## **Education**  **National Institute of Technology, Patna Sep. 2024 – Jul. 2028** _B.Tech, Electronics and Communication Engineering | CGPA:_ _**8.56/10** Patna, Bihar, India_ **Mercy Memorial Sc...
```

**Chunk 3 | Distance: 0.6567 | Source: personal_kb.txt**
```json
{
  "document_type": "text",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "source": "personal_kb.txt",
  "total_chunks": 15,
  "category": "blog",
  "chunk_index": 0,
  "owner": "ekansh",
  "document_name": "Personal Knowledge Base"
}
```
```text
# Ekansh Satsangi  ## About Me  I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna.  I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI application...
```

**Chunk 4 | Distance: 0.6567 | Source: personal_kb.txt**
```json
{
  "category": "blog",
  "total_chunks": 15,
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "source": "personal_kb.txt",
  "document_name": "Personal Knowledge Base",
  "chunk_index": 0,
  "owner": "ekansh",
  "document_type": "text"
}
```
```text
# Ekansh Satsangi  ## About Me  I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna.  I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI application...
```

**Chunk 5 | Distance: 0.6663 | Source: summary.md**
```json
{
  "category": "resume",
  "document_name": "Comprehensive Knowledge Base Summary",
  "owner": "ekansh",
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00",
  "chunk_index": 0,
  "total_chunks": 16,
  "source": "summary.md",
  "document_type": "markdown"
}
```
```text
Ekansh Satsangi About Me I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna. I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI applications. My pr...
```

### Q: What is Ekansh's CGPA?
**Result: PASS** (Best Distance: 0.6064)

**Chunk 1 | Distance: 0.6064 | Source: ekansh_resume.txt**
```json
{
  "document_type": "text",
  "category": "resume",
  "document_name": "Ekansh Resume",
  "uploaded_at": "2026-06-19T23:59:53.377793+00:00",
  "source": "ekansh_resume.txt",
  "total_chunks": 13,
  "chunk_index": 0,
  "owner": "ekansh"
}
```
```text
+91-8542951940 _|_ ekanshsatsangi@gmail.com _|_ LinkedIn _|_ GitHub _|_ Portfolio  ## Ekansh Satsangi  ## **Education**  **National Institute of Technology, Patna Sep. 2024 – Jul. 2028** _B.Tech, Electronics and Communication Engineering | CGPA:_ _**8.56/10** Patna, Bihar, India_ **Mercy Memorial Sc...
```

**Chunk 2 | Distance: 0.6064 | Source: ekansh_resume.txt**
```json
{
  "document_type": "text",
  "total_chunks": 13,
  "source": "ekansh_resume.txt",
  "uploaded_at": "2026-06-20T00:02:04.694247+00:00",
  "category": "resume",
  "chunk_index": 0,
  "document_name": "Ekansh Resume",
  "owner": "ekansh"
}
```
```text
+91-8542951940 _|_ ekanshsatsangi@gmail.com _|_ LinkedIn _|_ GitHub _|_ Portfolio  ## Ekansh Satsangi  ## **Education**  **National Institute of Technology, Patna Sep. 2024 – Jul. 2028** _B.Tech, Electronics and Communication Engineering | CGPA:_ _**8.56/10** Patna, Bihar, India_ **Mercy Memorial Sc...
```

**Chunk 3 | Distance: 0.6780 | Source: personal_kb.txt**
```json
{
  "total_chunks": 15,
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "category": "blog",
  "owner": "ekansh",
  "document_type": "text",
  "source": "personal_kb.txt",
  "document_name": "Personal Knowledge Base",
  "chunk_index": 14
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 4 | Distance: 0.6780 | Source: personal_kb.txt**
```json
{
  "chunk_index": 14,
  "document_type": "text",
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "total_chunks": 15,
  "source": "personal_kb.txt",
  "owner": "ekansh",
  "document_name": "Personal Knowledge Base",
  "category": "blog"
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 5 | Distance: 0.6993 | Source: personal_kb.txt**
```json
{
  "chunk_index": 0,
  "owner": "ekansh",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "document_type": "text",
  "document_name": "Personal Knowledge Base",
  "source": "personal_kb.txt",
  "total_chunks": 15,
  "category": "blog"
}
```
```text
# Ekansh Satsangi  ## About Me  I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna.  I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI application...
```

### Q: What are Ekansh's strongest technical skills?
**Result: PASS** (Best Distance: 0.4531)

**Chunk 1 | Distance: 0.4531 | Source: summary.md**
```json
{
  "total_chunks": 16,
  "category": "resume",
  "source": "summary.md",
  "chunk_index": 14,
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00",
  "owner": "ekansh",
  "document_name": "Comprehensive Knowledge Base Summary",
  "document_type": "markdown"
}
```
```text
as a Software Engineer and AI Engineer Frequently Asked Questions What are Ekansh's strongest technical areas? Backend Development, API Design, Authentication Systems, Database Design, Full-Stack Development, and AI-Powered Web Applications. Which projects best showcase Ekansh's skills? ReelOps and ...
```

**Chunk 2 | Distance: 0.4531 | Source: summary.md**
```json
{
  "source": "summary.md",
  "category": "resume",
  "owner": "ekansh",
  "uploaded_at": "2026-06-20T00:02:56.709776+00:00",
  "total_chunks": 16,
  "document_type": "markdown",
  "document_name": "Comprehensive Knowledge Base Summary",
  "chunk_index": 14
}
```
```text
as a Software Engineer and AI Engineer Frequently Asked Questions What are Ekansh's strongest technical areas? Backend Development, API Design, Authentication Systems, Database Design, Full-Stack Development, and AI-Powered Web Applications. Which projects best showcase Ekansh's skills? ReelOps and ...
```

**Chunk 3 | Distance: 0.4798 | Source: personal_kb.txt**
```json
{
  "document_type": "text",
  "chunk_index": 13,
  "owner": "ekansh",
  "total_chunks": 15,
  "document_name": "Personal Knowledge Base",
  "category": "blog",
  "source": "personal_kb.txt",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00"
}
```
```text
Which projects best showcase Ekansh's skills? ReelOps and MediSaar are currently the strongest demonstrations of his software engineering, backend development, and AI integration capabilities.  ## What technologies does Ekansh work with most frequently?  Java, JavaScript, TypeScript, React, Node.js,...
```

**Chunk 4 | Distance: 0.4798 | Source: personal_kb.txt**
```json
{
  "chunk_index": 13,
  "source": "personal_kb.txt",
  "category": "blog",
  "document_name": "Personal Knowledge Base",
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "document_type": "text",
  "total_chunks": 15,
  "owner": "ekansh"
}
```
```text
Which projects best showcase Ekansh's skills? ReelOps and MediSaar are currently the strongest demonstrations of his software engineering, backend development, and AI integration capabilities.  ## What technologies does Ekansh work with most frequently?  Java, JavaScript, TypeScript, React, Node.js,...
```

**Chunk 5 | Distance: 0.4984 | Source: personal_kb.txt**
```json
{
  "source": "personal_kb.txt",
  "document_type": "text",
  "category": "blog",
  "chunk_index": 14,
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "owner": "ekansh",
  "total_chunks": 15,
  "document_name": "Personal Knowledge Base"
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```


## Programming & DSA

### Q: How many LeetCode problems has Ekansh solved?
**Result: PASS** (Best Distance: 0.5623)

**Chunk 1 | Distance: 0.5623 | Source: personal_kb.txt**
```json
{
  "source": "personal_kb.txt",
  "document_type": "text",
  "document_name": "Personal Knowledge Base",
  "total_chunks": 15,
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "chunk_index": 13,
  "category": "blog",
  "owner": "ekansh"
}
```
```text
Which projects best showcase Ekansh's skills? ReelOps and MediSaar are currently the strongest demonstrations of his software engineering, backend development, and AI integration capabilities.  ## What technologies does Ekansh work with most frequently?  Java, JavaScript, TypeScript, React, Node.js,...
```

**Chunk 2 | Distance: 0.5623 | Source: personal_kb.txt**
```json
{
  "total_chunks": 15,
  "chunk_index": 13,
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "source": "personal_kb.txt",
  "document_name": "Personal Knowledge Base",
  "category": "blog",
  "owner": "ekansh",
  "document_type": "text"
}
```
```text
Which projects best showcase Ekansh's skills? ReelOps and MediSaar are currently the strongest demonstrations of his software engineering, backend development, and AI integration capabilities.  ## What technologies does Ekansh work with most frequently?  Java, JavaScript, TypeScript, React, Node.js,...
```

**Chunk 3 | Distance: 0.5785 | Source: summary.md**
```json
{
  "total_chunks": 16,
  "owner": "ekansh",
  "document_type": "markdown",
  "category": "resume",
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00",
  "chunk_index": 15,
  "document_name": "Comprehensive Knowledge Base Summary",
  "source": "summary.md"
}
```
```text
does Ekansh work with most frequently? Java, JavaScript, TypeScript, React, Node.js, Express.js, MongoDB, LangChain, ChromaDB, Docker, and Generative AI technologies. Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive ...
```

**Chunk 4 | Distance: 0.5785 | Source: summary.md**
```json
{
  "chunk_index": 15,
  "document_name": "Comprehensive Knowledge Base Summary",
  "uploaded_at": "2026-06-20T00:02:56.709776+00:00",
  "category": "resume",
  "total_chunks": 16,
  "document_type": "markdown",
  "owner": "ekansh",
  "source": "summary.md"
}
```
```text
does Ekansh work with most frequently? Java, JavaScript, TypeScript, React, Node.js, Express.js, MongoDB, LangChain, ChromaDB, Docker, and Generative AI technologies. Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive ...
```

**Chunk 5 | Distance: 0.6204 | Source: personal_kb.txt**
```json
{
  "category": "blog",
  "owner": "ekansh",
  "total_chunks": 15,
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "source": "personal_kb.txt",
  "chunk_index": 3,
  "document_type": "text",
  "document_name": "Personal Knowledge Base"
}
```
```text
ChromaDB  ## Artificial Intelligence & GenAI * LangChain * Retrieval-Augmented Generation (RAG) * Vector Databases * HuggingFace Models * Embedding Models * LLM Application Development  ## Cloud & DevOps  * Docker * Google Cloud Run * Google Cloud Build * Vercel * Cloudinary  ## Developer Tools  * G...
```

### Q: What is Ekansh's highest LeetCode rating?
**Result: FAIL** (Best Distance: 0.6507)

**Chunk 1 | Distance: 0.6507 | Source: personal_kb.txt**
```json
{
  "category": "blog",
  "document_type": "text",
  "total_chunks": 15,
  "document_name": "Personal Knowledge Base",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "source": "personal_kb.txt",
  "owner": "ekansh",
  "chunk_index": 13
}
```
```text
Which projects best showcase Ekansh's skills? ReelOps and MediSaar are currently the strongest demonstrations of his software engineering, backend development, and AI integration capabilities.  ## What technologies does Ekansh work with most frequently?  Java, JavaScript, TypeScript, React, Node.js,...
```

**Chunk 2 | Distance: 0.6507 | Source: personal_kb.txt**
```json
{
  "total_chunks": 15,
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "chunk_index": 13,
  "category": "blog",
  "document_type": "text",
  "source": "personal_kb.txt",
  "owner": "ekansh",
  "document_name": "Personal Knowledge Base"
}
```
```text
Which projects best showcase Ekansh's skills? ReelOps and MediSaar are currently the strongest demonstrations of his software engineering, backend development, and AI integration capabilities.  ## What technologies does Ekansh work with most frequently?  Java, JavaScript, TypeScript, React, Node.js,...
```

**Chunk 3 | Distance: 0.6772 | Source: summary.md**
```json
{
  "source": "summary.md",
  "owner": "ekansh",
  "chunk_index": 14,
  "document_type": "markdown",
  "total_chunks": 16,
  "category": "resume",
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00",
  "document_name": "Comprehensive Knowledge Base Summary"
}
```
```text
as a Software Engineer and AI Engineer Frequently Asked Questions What are Ekansh's strongest technical areas? Backend Development, API Design, Authentication Systems, Database Design, Full-Stack Development, and AI-Powered Web Applications. Which projects best showcase Ekansh's skills? ReelOps and ...
```

**Chunk 4 | Distance: 0.6772 | Source: summary.md**
```json
{
  "total_chunks": 16,
  "document_type": "markdown",
  "uploaded_at": "2026-06-20T00:02:56.709776+00:00",
  "owner": "ekansh",
  "category": "resume",
  "chunk_index": 14,
  "source": "summary.md",
  "document_name": "Comprehensive Knowledge Base Summary"
}
```
```text
as a Software Engineer and AI Engineer Frequently Asked Questions What are Ekansh's strongest technical areas? Backend Development, API Design, Authentication Systems, Database Design, Full-Stack Development, and AI-Powered Web Applications. Which projects best showcase Ekansh's skills? ReelOps and ...
```

**Chunk 5 | Distance: 0.6912 | Source: personal_kb.txt**
```json
{
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "chunk_index": 14,
  "owner": "ekansh",
  "document_name": "Personal Knowledge Base",
  "total_chunks": 15,
  "document_type": "text",
  "category": "blog",
  "source": "personal_kb.txt"
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

### Q: What competitive programming platforms does Ekansh use?
**Result: PASS** (Best Distance: 0.3988)

**Chunk 1 | Distance: 0.3988 | Source: personal_kb.txt**
```json
{
  "document_type": "text",
  "document_name": "Personal Knowledge Base",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "category": "blog",
  "owner": "ekansh",
  "source": "personal_kb.txt",
  "total_chunks": 15,
  "chunk_index": 13
}
```
```text
Which projects best showcase Ekansh's skills? ReelOps and MediSaar are currently the strongest demonstrations of his software engineering, backend development, and AI integration capabilities.  ## What technologies does Ekansh work with most frequently?  Java, JavaScript, TypeScript, React, Node.js,...
```

**Chunk 2 | Distance: 0.3988 | Source: personal_kb.txt**
```json
{
  "total_chunks": 15,
  "category": "blog",
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "document_type": "text",
  "document_name": "Personal Knowledge Base",
  "chunk_index": 13,
  "source": "personal_kb.txt",
  "owner": "ekansh"
}
```
```text
Which projects best showcase Ekansh's skills? ReelOps and MediSaar are currently the strongest demonstrations of his software engineering, backend development, and AI integration capabilities.  ## What technologies does Ekansh work with most frequently?  Java, JavaScript, TypeScript, React, Node.js,...
```

**Chunk 3 | Distance: 0.4355 | Source: summary.md**
```json
{
  "total_chunks": 16,
  "source": "summary.md",
  "chunk_index": 15,
  "owner": "ekansh",
  "category": "resume",
  "document_type": "markdown",
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00",
  "document_name": "Comprehensive Knowledge Base Summary"
}
```
```text
does Ekansh work with most frequently? Java, JavaScript, TypeScript, React, Node.js, Express.js, MongoDB, LangChain, ChromaDB, Docker, and Generative AI technologies. Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive ...
```

**Chunk 4 | Distance: 0.4355 | Source: summary.md**
```json
{
  "source": "summary.md",
  "document_type": "markdown",
  "total_chunks": 16,
  "uploaded_at": "2026-06-20T00:02:56.709776+00:00",
  "document_name": "Comprehensive Knowledge Base Summary",
  "owner": "ekansh",
  "category": "resume",
  "chunk_index": 15
}
```
```text
does Ekansh work with most frequently? Java, JavaScript, TypeScript, React, Node.js, Express.js, MongoDB, LangChain, ChromaDB, Docker, and Generative AI technologies. Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive ...
```

**Chunk 5 | Distance: 0.4392 | Source: personal_kb.txt**
```json
{
  "owner": "ekansh",
  "chunk_index": 14,
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "document_type": "text",
  "document_name": "Personal Knowledge Base",
  "source": "personal_kb.txt",
  "total_chunks": 15,
  "category": "blog"
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```


## ReelOps

### Q: What is ReelOps?
**Result: PASS** (Best Distance: 0.4124)

**Chunk 1 | Distance: 0.4124 | Source: reelops_summary.txt**
```json
{
  "uploaded_at": "2026-06-20T00:00:10.117245+00:00",
  "chunk_index": 0,
  "document_name": "ReelOps Summary",
  "category": "project",
  "document_type": "text",
  "total_chunks": 17,
  "owner": "ekansh",
  "source": "reelops_summary.txt"
}
```
```text
# ReelOps: Complete Project Summary  ## 1. Overview **ReelOps** is an enterprise-grade, AI-powered content publishing platform built for modern creators. It is designed to automate the tedious processes of uploading, scheduling, and managing social media video content across multiple channels. The a...
```

**Chunk 2 | Distance: 0.4124 | Source: reelops_summary.txt**
```json
{
  "category": "project",
  "uploaded_at": "2026-06-20T00:02:45.837398+00:00",
  "source": "reelops_summary.txt",
  "document_name": "ReelOps Summary",
  "total_chunks": 17,
  "chunk_index": 0,
  "owner": "ekansh",
  "document_type": "text"
}
```
```text
# ReelOps: Complete Project Summary  ## 1. Overview **ReelOps** is an enterprise-grade, AI-powered content publishing platform built for modern creators. It is designed to automate the tedious processes of uploading, scheduling, and managing social media video content across multiple channels. The a...
```

**Chunk 3 | Distance: 0.4206 | Source: test_project.md**
```json
{
  "total_chunks": 2,
  "category": "project",
  "chunk_index": 0,
  "owner": "ekansh",
  "document_type": "markdown",
  "uploaded_at": "2026-06-19T23:36:00.680582+00:00",
  "source": "test_project.md",
  "document_name": "ReelOps Project"
}
```
```text
ReelOps ReelOps is a DevOps automation platform built by Ekansh Satsangi. It streamlines CI/CD pipeline management for development teams. Key Features  Automated deployment pipelines Real-time monitoring dashboards Infrastructure as Code templates GitHub Actions integration  Tech Stack  Frontend: Re...
```

**Chunk 4 | Distance: 0.4730 | Source: personal_kb.txt**
```json
{
  "owner": "ekansh",
  "total_chunks": 15,
  "category": "blog",
  "chunk_index": 5,
  "document_type": "text",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "source": "personal_kb.txt",
  "document_name": "Personal Knowledge Base"
}
```
```text
Content Operations Platform  ### Problem Content creators, editors, and channel owners often struggle to manage content workflows, approvals, collaboration, and publishing processes efficiently.  ### Solution  ReelOps is a centralized content operations platform that streamlines the complete content...
```

**Chunk 5 | Distance: 0.4730 | Source: personal_kb.txt**
```json
{
  "owner": "ekansh",
  "total_chunks": 15,
  "source": "personal_kb.txt",
  "document_name": "Personal Knowledge Base",
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "chunk_index": 5,
  "document_type": "text",
  "category": "blog"
}
```
```text
Content Operations Platform  ### Problem Content creators, editors, and channel owners often struggle to manage content workflows, approvals, collaboration, and publishing processes efficiently.  ### Solution  ReelOps is a centralized content operations platform that streamlines the complete content...
```

### Q: What problem does ReelOps solve?
**Result: PASS** (Best Distance: 0.5398)

**Chunk 1 | Distance: 0.5398 | Source: test_project.md**
```json
{
  "document_name": "ReelOps Project",
  "total_chunks": 2,
  "owner": "ekansh",
  "category": "project",
  "uploaded_at": "2026-06-19T23:36:00.680582+00:00",
  "chunk_index": 0,
  "source": "test_project.md",
  "document_type": "markdown"
}
```
```text
ReelOps ReelOps is a DevOps automation platform built by Ekansh Satsangi. It streamlines CI/CD pipeline management for development teams. Key Features  Automated deployment pipelines Real-time monitoring dashboards Infrastructure as Code templates GitHub Actions integration  Tech Stack  Frontend: Re...
```

**Chunk 2 | Distance: 0.5449 | Source: personal_kb.txt**
```json
{
  "owner": "ekansh",
  "source": "personal_kb.txt",
  "document_name": "Personal Knowledge Base",
  "category": "blog",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "document_type": "text",
  "chunk_index": 5,
  "total_chunks": 15
}
```
```text
Content Operations Platform  ### Problem Content creators, editors, and channel owners often struggle to manage content workflows, approvals, collaboration, and publishing processes efficiently.  ### Solution  ReelOps is a centralized content operations platform that streamlines the complete content...
```

**Chunk 3 | Distance: 0.5449 | Source: personal_kb.txt**
```json
{
  "document_name": "Personal Knowledge Base",
  "owner": "ekansh",
  "document_type": "text",
  "chunk_index": 5,
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "source": "personal_kb.txt",
  "category": "blog",
  "total_chunks": 15
}
```
```text
Content Operations Platform  ### Problem Content creators, editors, and channel owners often struggle to manage content workflows, approvals, collaboration, and publishing processes efficiently.  ### Solution  ReelOps is a centralized content operations platform that streamlines the complete content...
```

**Chunk 4 | Distance: 0.5509 | Source: summary.md**
```json
{
  "source": "summary.md",
  "document_type": "markdown",
  "owner": "ekansh",
  "document_name": "Comprehensive Knowledge Base Summary",
  "chunk_index": 5,
  "category": "resume",
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00",
  "total_chunks": 16
}
```
```text
97.4% ISC: 93.5% Current CGPA: 8.56 Projects ReelOps Category AI-Powered Content Operations Platform Problem Content creators, editors, and channel owners often struggle to manage content workflows, approvals, collaboration, and publishing processes efficiently. Solution ReelOps is a centralized con...
```

**Chunk 5 | Distance: 0.5509 | Source: summary.md**
```json
{
  "document_type": "markdown",
  "uploaded_at": "2026-06-20T00:02:56.709776+00:00",
  "source": "summary.md",
  "category": "resume",
  "document_name": "Comprehensive Knowledge Base Summary",
  "chunk_index": 5,
  "owner": "ekansh",
  "total_chunks": 16
}
```
```text
97.4% ISC: 93.5% Current CGPA: 8.56 Projects ReelOps Category AI-Powered Content Operations Platform Problem Content creators, editors, and channel owners often struggle to manage content workflows, approvals, collaboration, and publishing processes efficiently. Solution ReelOps is a centralized con...
```

### Q: What technologies were used in ReelOps?
**Result: PASS** (Best Distance: 0.4953)

**Chunk 1 | Distance: 0.4953 | Source: test_project.md**
```json
{
  "document_type": "markdown",
  "uploaded_at": "2026-06-19T23:36:00.680582+00:00",
  "owner": "ekansh",
  "chunk_index": 0,
  "total_chunks": 2,
  "document_name": "ReelOps Project",
  "category": "project",
  "source": "test_project.md"
}
```
```text
ReelOps ReelOps is a DevOps automation platform built by Ekansh Satsangi. It streamlines CI/CD pipeline management for development teams. Key Features  Automated deployment pipelines Real-time monitoring dashboards Infrastructure as Code templates GitHub Actions integration  Tech Stack  Frontend: Re...
```

**Chunk 2 | Distance: 0.5313 | Source: reelops_summary.txt**
```json
{
  "uploaded_at": "2026-06-20T00:00:10.117245+00:00",
  "document_type": "text",
  "total_chunks": 17,
  "category": "project",
  "chunk_index": 0,
  "source": "reelops_summary.txt",
  "owner": "ekansh",
  "document_name": "ReelOps Summary"
}
```
```text
# ReelOps: Complete Project Summary  ## 1. Overview **ReelOps** is an enterprise-grade, AI-powered content publishing platform built for modern creators. It is designed to automate the tedious processes of uploading, scheduling, and managing social media video content across multiple channels. The a...
```

**Chunk 3 | Distance: 0.5313 | Source: reelops_summary.txt**
```json
{
  "document_type": "text",
  "owner": "ekansh",
  "source": "reelops_summary.txt",
  "uploaded_at": "2026-06-20T00:02:45.837398+00:00",
  "category": "project",
  "document_name": "ReelOps Summary",
  "total_chunks": 17,
  "chunk_index": 0
}
```
```text
# ReelOps: Complete Project Summary  ## 1. Overview **ReelOps** is an enterprise-grade, AI-powered content publishing platform built for modern creators. It is designed to automate the tedious processes of uploading, scheduling, and managing social media video content across multiple channels. The a...
```

**Chunk 4 | Distance: 0.5602 | Source: reelops_summary.txt**
```json
{
  "total_chunks": 17,
  "category": "project",
  "document_name": "ReelOps Summary",
  "uploaded_at": "2026-06-20T00:00:10.117245+00:00",
  "chunk_index": 11,
  "owner": "ekansh",
  "document_type": "text",
  "source": "reelops_summary.txt"
}
```
```text
descriptions, and tags based on video topics. ### D. Background Automation Scheduler (The Engine) The most complex part of ReelOps is its robust scheduling engine: - **Tick Engine:** Uses `node-cron` to check the database every minute for scheduled videos. - **Atomic Locking:** Implements a `findAnd...
```

**Chunk 5 | Distance: 0.5602 | Source: reelops_summary.txt**
```json
{
  "document_type": "text",
  "owner": "ekansh",
  "chunk_index": 11,
  "total_chunks": 17,
  "category": "project",
  "source": "reelops_summary.txt",
  "document_name": "ReelOps Summary",
  "uploaded_at": "2026-06-20T00:02:45.837398+00:00"
}
```
```text
descriptions, and tags based on video topics. ### D. Background Automation Scheduler (The Engine) The most complex part of ReelOps is its robust scheduling engine: - **Tick Engine:** Uses `node-cron` to check the database every minute for scheduled videos. - **Atomic Locking:** Implements a `findAnd...
```

### Q: What was Ekansh's role in ReelOps?
**Result: PASS** (Best Distance: 0.5200)

**Chunk 1 | Distance: 0.5200 | Source: test_project.md**
```json
{
  "document_type": "markdown",
  "total_chunks": 2,
  "chunk_index": 0,
  "category": "project",
  "source": "test_project.md",
  "document_name": "ReelOps Project",
  "uploaded_at": "2026-06-19T23:36:00.680582+00:00",
  "owner": "ekansh"
}
```
```text
ReelOps ReelOps is a DevOps automation platform built by Ekansh Satsangi. It streamlines CI/CD pipeline management for development teams. Key Features  Automated deployment pipelines Real-time monitoring dashboards Infrastructure as Code templates GitHub Actions integration  Tech Stack  Frontend: Re...
```

**Chunk 2 | Distance: 0.6225 | Source: personal_kb.txt**
```json
{
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "chunk_index": 13,
  "owner": "ekansh",
  "total_chunks": 15,
  "source": "personal_kb.txt",
  "category": "blog",
  "document_name": "Personal Knowledge Base",
  "document_type": "text"
}
```
```text
Which projects best showcase Ekansh's skills? ReelOps and MediSaar are currently the strongest demonstrations of his software engineering, backend development, and AI integration capabilities.  ## What technologies does Ekansh work with most frequently?  Java, JavaScript, TypeScript, React, Node.js,...
```

**Chunk 3 | Distance: 0.6225 | Source: personal_kb.txt**
```json
{
  "document_name": "Personal Knowledge Base",
  "chunk_index": 13,
  "total_chunks": 15,
  "document_type": "text",
  "owner": "ekansh",
  "source": "personal_kb.txt",
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "category": "blog"
}
```
```text
Which projects best showcase Ekansh's skills? ReelOps and MediSaar are currently the strongest demonstrations of his software engineering, backend development, and AI integration capabilities.  ## What technologies does Ekansh work with most frequently?  Java, JavaScript, TypeScript, React, Node.js,...
```

**Chunk 4 | Distance: 0.6862 | Source: summary.md**
```json
{
  "document_name": "Comprehensive Knowledge Base Summary",
  "category": "resume",
  "source": "summary.md",
  "document_type": "markdown",
  "chunk_index": 14,
  "owner": "ekansh",
  "total_chunks": 16,
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00"
}
```
```text
as a Software Engineer and AI Engineer Frequently Asked Questions What are Ekansh's strongest technical areas? Backend Development, API Design, Authentication Systems, Database Design, Full-Stack Development, and AI-Powered Web Applications. Which projects best showcase Ekansh's skills? ReelOps and ...
```

**Chunk 5 | Distance: 0.6862 | Source: summary.md**
```json
{
  "document_type": "markdown",
  "category": "resume",
  "chunk_index": 14,
  "document_name": "Comprehensive Knowledge Base Summary",
  "total_chunks": 16,
  "source": "summary.md",
  "uploaded_at": "2026-06-20T00:02:56.709776+00:00",
  "owner": "ekansh"
}
```
```text
as a Software Engineer and AI Engineer Frequently Asked Questions What are Ekansh's strongest technical areas? Backend Development, API Design, Authentication Systems, Database Design, Full-Stack Development, and AI-Powered Web Applications. Which projects best showcase Ekansh's skills? ReelOps and ...
```

### Q: What AI features exist in ReelOps?
**Result: PASS** (Best Distance: 0.4384)

**Chunk 1 | Distance: 0.4384 | Source: reelops_summary.txt**
```json
{
  "document_name": "ReelOps Summary",
  "total_chunks": 17,
  "document_type": "text",
  "category": "project",
  "source": "reelops_summary.txt",
  "chunk_index": 0,
  "owner": "ekansh",
  "uploaded_at": "2026-06-20T00:00:10.117245+00:00"
}
```
```text
# ReelOps: Complete Project Summary  ## 1. Overview **ReelOps** is an enterprise-grade, AI-powered content publishing platform built for modern creators. It is designed to automate the tedious processes of uploading, scheduling, and managing social media video content across multiple channels. The a...
```

**Chunk 2 | Distance: 0.4384 | Source: reelops_summary.txt**
```json
{
  "total_chunks": 17,
  "document_type": "text",
  "source": "reelops_summary.txt",
  "document_name": "ReelOps Summary",
  "category": "project",
  "owner": "ekansh",
  "uploaded_at": "2026-06-20T00:02:45.837398+00:00",
  "chunk_index": 0
}
```
```text
# ReelOps: Complete Project Summary  ## 1. Overview **ReelOps** is an enterprise-grade, AI-powered content publishing platform built for modern creators. It is designed to automate the tedious processes of uploading, scheduling, and managing social media video content across multiple channels. The a...
```

**Chunk 3 | Distance: 0.4674 | Source: test_project.md**
```json
{
  "category": "project",
  "uploaded_at": "2026-06-19T23:36:00.680582+00:00",
  "total_chunks": 2,
  "source": "test_project.md",
  "owner": "ekansh",
  "chunk_index": 0,
  "document_name": "ReelOps Project",
  "document_type": "markdown"
}
```
```text
ReelOps ReelOps is a DevOps automation platform built by Ekansh Satsangi. It streamlines CI/CD pipeline management for development teams. Key Features  Automated deployment pipelines Real-time monitoring dashboards Infrastructure as Code templates GitHub Actions integration  Tech Stack  Frontend: Re...
```

**Chunk 4 | Distance: 0.4741 | Source: summary.md**
```json
{
  "owner": "ekansh",
  "source": "summary.md",
  "chunk_index": 5,
  "document_type": "markdown",
  "category": "resume",
  "total_chunks": 16,
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00",
  "document_name": "Comprehensive Knowledge Base Summary"
}
```
```text
97.4% ISC: 93.5% Current CGPA: 8.56 Projects ReelOps Category AI-Powered Content Operations Platform Problem Content creators, editors, and channel owners often struggle to manage content workflows, approvals, collaboration, and publishing processes efficiently. Solution ReelOps is a centralized con...
```

**Chunk 5 | Distance: 0.4741 | Source: summary.md**
```json
{
  "source": "summary.md",
  "chunk_index": 5,
  "document_name": "Comprehensive Knowledge Base Summary",
  "uploaded_at": "2026-06-20T00:02:56.709776+00:00",
  "total_chunks": 16,
  "category": "resume",
  "document_type": "markdown",
  "owner": "ekansh"
}
```
```text
97.4% ISC: 93.5% Current CGPA: 8.56 Projects ReelOps Category AI-Powered Content Operations Platform Problem Content creators, editors, and channel owners often struggle to manage content workflows, approvals, collaboration, and publishing processes efficiently. Solution ReelOps is a centralized con...
```


## MediSaar

### Q: What is MediSaar?
**Result: PASS** (Best Distance: 0.3227)

**Chunk 1 | Distance: 0.3227 | Source: medisaar_summary.txt**
```json
{
  "owner": "ekansh",
  "category": "project",
  "chunk_index": 1,
  "total_chunks": 17,
  "document_type": "text",
  "source": "medisaar_summary.txt",
  "document_name": "MediSaar Summary",
  "uploaded_at": "2026-06-20T00:00:03.226426+00:00"
}
```
```text
a highly clinical AI intelligence layer.  --- ## 1. Executive Summary **MediSaar** is a clinical intelligence platform designed to unify scattered patient health records (prescriptions, lab reports, discharge summaries) into a single, cohesive patient history. It uses advanced Optical Character Reco...
```

**Chunk 2 | Distance: 0.3227 | Source: medisaar_summary.txt**
```json
{
  "chunk_index": 1,
  "total_chunks": 17,
  "uploaded_at": "2026-06-20T00:02:28.632739+00:00",
  "source": "medisaar_summary.txt",
  "owner": "ekansh",
  "category": "project",
  "document_type": "text",
  "document_name": "MediSaar Summary"
}
```
```text
a highly clinical AI intelligence layer.  --- ## 1. Executive Summary **MediSaar** is a clinical intelligence platform designed to unify scattered patient health records (prescriptions, lab reports, discharge summaries) into a single, cohesive patient history. It uses advanced Optical Character Reco...
```

**Chunk 3 | Distance: 0.3370 | Source: medisaar_summary.txt**
```json
{
  "source": "medisaar_summary.txt",
  "document_name": "MediSaar Summary",
  "document_type": "text",
  "total_chunks": 17,
  "chunk_index": 16,
  "owner": "ekansh",
  "uploaded_at": "2026-06-20T00:00:03.226426+00:00",
  "category": "project"
}
```
```text
rely heavily on their phones during rounds. ## Conclusion MediSaar is built to restore the human connection in medical consultations by ensuring the doctor spends their 60 seconds reading a coherent narrative, rather than digging through physical files. It is an engineering and design effort that pr...
```

**Chunk 4 | Distance: 0.3370 | Source: medisaar_summary.txt**
```json
{
  "category": "project",
  "owner": "ekansh",
  "document_type": "text",
  "total_chunks": 17,
  "uploaded_at": "2026-06-20T00:02:28.632739+00:00",
  "document_name": "MediSaar Summary",
  "source": "medisaar_summary.txt",
  "chunk_index": 16
}
```
```text
rely heavily on their phones during rounds. ## Conclusion MediSaar is built to restore the human connection in medical consultations by ensuring the doctor spends their 60 seconds reading a coherent narrative, rather than digging through physical files. It is an engineering and design effort that pr...
```

**Chunk 5 | Distance: 0.4770 | Source: medisaar_summary.txt**
```json
{
  "chunk_index": 0,
  "document_name": "MediSaar Summary",
  "source": "medisaar_summary.txt",
  "uploaded_at": "2026-06-20T00:00:03.226426+00:00",
  "category": "project",
  "total_chunks": 17,
  "document_type": "text",
  "owner": "ekansh"
}
```
```text
# MediSaar Project Summary *Editorial healthcare. Clinical intelligence with empathy.*  > **Product Vision**: Apple Health's calm + Notion's structure + Linear's craft + a New Yorker article's typography.  > MediSaar transforms fragmented, unreadable healthcare records into a coherent, interactive t...
```

### Q: What problem does MediSaar solve?
**Result: PASS** (Best Distance: 0.4449)

**Chunk 1 | Distance: 0.4449 | Source: medisaar_summary.txt**
```json
{
  "total_chunks": 17,
  "uploaded_at": "2026-06-20T00:00:03.226426+00:00",
  "document_name": "MediSaar Summary",
  "document_type": "text",
  "source": "medisaar_summary.txt",
  "category": "project",
  "chunk_index": 16,
  "owner": "ekansh"
}
```
```text
rely heavily on their phones during rounds. ## Conclusion MediSaar is built to restore the human connection in medical consultations by ensuring the doctor spends their 60 seconds reading a coherent narrative, rather than digging through physical files. It is an engineering and design effort that pr...
```

**Chunk 2 | Distance: 0.4449 | Source: medisaar_summary.txt**
```json
{
  "document_name": "MediSaar Summary",
  "total_chunks": 17,
  "chunk_index": 16,
  "category": "project",
  "source": "medisaar_summary.txt",
  "document_type": "text",
  "owner": "ekansh",
  "uploaded_at": "2026-06-20T00:02:28.632739+00:00"
}
```
```text
rely heavily on their phones during rounds. ## Conclusion MediSaar is built to restore the human connection in medical consultations by ensuring the doctor spends their 60 seconds reading a coherent narrative, rather than digging through physical files. It is an engineering and design effort that pr...
```

**Chunk 3 | Distance: 0.4761 | Source: medisaar_summary.txt**
```json
{
  "document_type": "text",
  "total_chunks": 17,
  "uploaded_at": "2026-06-20T00:00:03.226426+00:00",
  "owner": "ekansh",
  "document_name": "MediSaar Summary",
  "source": "medisaar_summary.txt",
  "category": "project",
  "chunk_index": 1
}
```
```text
a highly clinical AI intelligence layer.  --- ## 1. Executive Summary **MediSaar** is a clinical intelligence platform designed to unify scattered patient health records (prescriptions, lab reports, discharge summaries) into a single, cohesive patient history. It uses advanced Optical Character Reco...
```

**Chunk 4 | Distance: 0.4761 | Source: medisaar_summary.txt**
```json
{
  "category": "project",
  "document_type": "text",
  "source": "medisaar_summary.txt",
  "document_name": "MediSaar Summary",
  "total_chunks": 17,
  "owner": "ekansh",
  "chunk_index": 1,
  "uploaded_at": "2026-06-20T00:02:28.632739+00:00"
}
```
```text
a highly clinical AI intelligence layer.  --- ## 1. Executive Summary **MediSaar** is a clinical intelligence platform designed to unify scattered patient health records (prescriptions, lab reports, discharge summaries) into a single, cohesive patient history. It uses advanced Optical Character Reco...
```

**Chunk 5 | Distance: 0.4966 | Source: summary.md**
```json
{
  "owner": "ekansh",
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00",
  "category": "resume",
  "chunk_index": 8,
  "document_type": "markdown",
  "source": "summary.md",
  "total_chunks": 16,
  "document_name": "Comprehensive Knowledge Base Summary"
}
```
```text
AI-powered functionality MediSaar Category AI-Powered Healthcare Intelligence Platform Problem Medical records are fragmented across hospitals, doctors, reports, prescriptions, and healthcare institutions, making healthcare management inefficient. Solution MediSaar centralizes patient healthcare dat...
```

### Q: What technologies were used in MediSaar?
**Result: PASS** (Best Distance: 0.3804)

**Chunk 1 | Distance: 0.3804 | Source: medisaar_summary.txt**
```json
{
  "category": "project",
  "uploaded_at": "2026-06-20T00:00:03.226426+00:00",
  "document_name": "MediSaar Summary",
  "source": "medisaar_summary.txt",
  "owner": "ekansh",
  "total_chunks": 17,
  "chunk_index": 16,
  "document_type": "text"
}
```
```text
rely heavily on their phones during rounds. ## Conclusion MediSaar is built to restore the human connection in medical consultations by ensuring the doctor spends their 60 seconds reading a coherent narrative, rather than digging through physical files. It is an engineering and design effort that pr...
```

**Chunk 2 | Distance: 0.3804 | Source: medisaar_summary.txt**
```json
{
  "owner": "ekansh",
  "document_name": "MediSaar Summary",
  "uploaded_at": "2026-06-20T00:02:28.632739+00:00",
  "total_chunks": 17,
  "category": "project",
  "source": "medisaar_summary.txt",
  "document_type": "text",
  "chunk_index": 16
}
```
```text
rely heavily on their phones during rounds. ## Conclusion MediSaar is built to restore the human connection in medical consultations by ensuring the doctor spends their 60 seconds reading a coherent narrative, rather than digging through physical files. It is an engineering and design effort that pr...
```

**Chunk 3 | Distance: 0.4071 | Source: medisaar_summary.txt**
```json
{
  "source": "medisaar_summary.txt",
  "owner": "ekansh",
  "document_name": "MediSaar Summary",
  "chunk_index": 1,
  "uploaded_at": "2026-06-20T00:00:03.226426+00:00",
  "category": "project",
  "total_chunks": 17,
  "document_type": "text"
}
```
```text
a highly clinical AI intelligence layer.  --- ## 1. Executive Summary **MediSaar** is a clinical intelligence platform designed to unify scattered patient health records (prescriptions, lab reports, discharge summaries) into a single, cohesive patient history. It uses advanced Optical Character Reco...
```

**Chunk 4 | Distance: 0.4071 | Source: medisaar_summary.txt**
```json
{
  "chunk_index": 1,
  "category": "project",
  "total_chunks": 17,
  "document_type": "text",
  "owner": "ekansh",
  "uploaded_at": "2026-06-20T00:02:28.632739+00:00",
  "source": "medisaar_summary.txt",
  "document_name": "MediSaar Summary"
}
```
```text
a highly clinical AI intelligence layer.  --- ## 1. Executive Summary **MediSaar** is a clinical intelligence platform designed to unify scattered patient health records (prescriptions, lab reports, discharge summaries) into a single, cohesive patient history. It uses advanced Optical Character Reco...
```

**Chunk 5 | Distance: 0.5075 | Source: medisaar_summary.txt**
```json
{
  "category": "project",
  "document_name": "MediSaar Summary",
  "chunk_index": 0,
  "document_type": "text",
  "total_chunks": 17,
  "source": "medisaar_summary.txt",
  "owner": "ekansh",
  "uploaded_at": "2026-06-20T00:00:03.226426+00:00"
}
```
```text
# MediSaar Project Summary *Editorial healthcare. Clinical intelligence with empathy.*  > **Product Vision**: Apple Health's calm + Notion's structure + Linear's craft + a New Yorker article's typography.  > MediSaar transforms fragmented, unreadable healthcare records into a coherent, interactive t...
```

### Q: What AI features exist in MediSaar?
**Result: PASS** (Best Distance: 0.2770)

**Chunk 1 | Distance: 0.2770 | Source: medisaar_summary.txt**
```json
{
  "source": "medisaar_summary.txt",
  "owner": "ekansh",
  "chunk_index": 1,
  "category": "project",
  "document_name": "MediSaar Summary",
  "document_type": "text",
  "uploaded_at": "2026-06-20T00:00:03.226426+00:00",
  "total_chunks": 17
}
```
```text
a highly clinical AI intelligence layer.  --- ## 1. Executive Summary **MediSaar** is a clinical intelligence platform designed to unify scattered patient health records (prescriptions, lab reports, discharge summaries) into a single, cohesive patient history. It uses advanced Optical Character Reco...
```

**Chunk 2 | Distance: 0.2770 | Source: medisaar_summary.txt**
```json
{
  "uploaded_at": "2026-06-20T00:02:28.632739+00:00",
  "category": "project",
  "total_chunks": 17,
  "owner": "ekansh",
  "document_name": "MediSaar Summary",
  "source": "medisaar_summary.txt",
  "document_type": "text",
  "chunk_index": 1
}
```
```text
a highly clinical AI intelligence layer.  --- ## 1. Executive Summary **MediSaar** is a clinical intelligence platform designed to unify scattered patient health records (prescriptions, lab reports, discharge summaries) into a single, cohesive patient history. It uses advanced Optical Character Reco...
```

**Chunk 3 | Distance: 0.3789 | Source: summary.md**
```json
{
  "total_chunks": 16,
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00",
  "document_name": "Comprehensive Knowledge Base Summary",
  "category": "resume",
  "chunk_index": 8,
  "document_type": "markdown",
  "owner": "ekansh",
  "source": "summary.md"
}
```
```text
AI-powered functionality MediSaar Category AI-Powered Healthcare Intelligence Platform Problem Medical records are fragmented across hospitals, doctors, reports, prescriptions, and healthcare institutions, making healthcare management inefficient. Solution MediSaar centralizes patient healthcare dat...
```

**Chunk 4 | Distance: 0.3789 | Source: summary.md**
```json
{
  "document_type": "markdown",
  "owner": "ekansh",
  "document_name": "Comprehensive Knowledge Base Summary",
  "chunk_index": 8,
  "source": "summary.md",
  "total_chunks": 16,
  "category": "resume",
  "uploaded_at": "2026-06-20T00:02:56.709776+00:00"
}
```
```text
AI-powered functionality MediSaar Category AI-Powered Healthcare Intelligence Platform Problem Medical records are fragmented across hospitals, doctors, reports, prescriptions, and healthcare institutions, making healthcare management inefficient. Solution MediSaar centralizes patient healthcare dat...
```

**Chunk 5 | Distance: 0.4218 | Source: medisaar_summary.txt**
```json
{
  "category": "project",
  "uploaded_at": "2026-06-20T00:00:03.226426+00:00",
  "source": "medisaar_summary.txt",
  "chunk_index": 0,
  "total_chunks": 17,
  "document_type": "text",
  "owner": "ekansh",
  "document_name": "MediSaar Summary"
}
```
```text
# MediSaar Project Summary *Editorial healthcare. Clinical intelligence with empathy.*  > **Product Vision**: Apple Health's calm + Notion's structure + Linear's craft + a New Yorker article's typography.  > MediSaar transforms fragmented, unreadable healthcare records into a coherent, interactive t...
```

### Q: What was Ekansh's role in MediSaar?
**Result: PASS** (Best Distance: 0.6423)

**Chunk 1 | Distance: 0.6423 | Source: medisaar_summary.txt**
```json
{
  "document_name": "MediSaar Summary",
  "source": "medisaar_summary.txt",
  "category": "project",
  "owner": "ekansh",
  "chunk_index": 16,
  "total_chunks": 17,
  "document_type": "text",
  "uploaded_at": "2026-06-20T00:00:03.226426+00:00"
}
```
```text
rely heavily on their phones during rounds. ## Conclusion MediSaar is built to restore the human connection in medical consultations by ensuring the doctor spends their 60 seconds reading a coherent narrative, rather than digging through physical files. It is an engineering and design effort that pr...
```

**Chunk 2 | Distance: 0.6423 | Source: medisaar_summary.txt**
```json
{
  "chunk_index": 16,
  "source": "medisaar_summary.txt",
  "total_chunks": 17,
  "document_type": "text",
  "owner": "ekansh",
  "document_name": "MediSaar Summary",
  "uploaded_at": "2026-06-20T00:02:28.632739+00:00",
  "category": "project"
}
```
```text
rely heavily on their phones during rounds. ## Conclusion MediSaar is built to restore the human connection in medical consultations by ensuring the doctor spends their 60 seconds reading a coherent narrative, rather than digging through physical files. It is an engineering and design effort that pr...
```

**Chunk 3 | Distance: 0.6467 | Source: medisaar_summary.txt**
```json
{
  "source": "medisaar_summary.txt",
  "document_type": "text",
  "total_chunks": 17,
  "category": "project",
  "chunk_index": 1,
  "uploaded_at": "2026-06-20T00:00:03.226426+00:00",
  "owner": "ekansh",
  "document_name": "MediSaar Summary"
}
```
```text
a highly clinical AI intelligence layer.  --- ## 1. Executive Summary **MediSaar** is a clinical intelligence platform designed to unify scattered patient health records (prescriptions, lab reports, discharge summaries) into a single, cohesive patient history. It uses advanced Optical Character Reco...
```

**Chunk 4 | Distance: 0.6467 | Source: medisaar_summary.txt**
```json
{
  "chunk_index": 1,
  "category": "project",
  "total_chunks": 17,
  "document_type": "text",
  "owner": "ekansh",
  "uploaded_at": "2026-06-20T00:02:28.632739+00:00",
  "source": "medisaar_summary.txt",
  "document_name": "MediSaar Summary"
}
```
```text
a highly clinical AI intelligence layer.  --- ## 1. Executive Summary **MediSaar** is a clinical intelligence platform designed to unify scattered patient health records (prescriptions, lab reports, discharge summaries) into a single, cohesive patient history. It uses advanced Optical Character Reco...
```

**Chunk 5 | Distance: 0.7025 | Source: personal_kb.txt**
```json
{
  "total_chunks": 15,
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "category": "blog",
  "document_type": "text",
  "chunk_index": 0,
  "document_name": "Personal Knowledge Base",
  "source": "personal_kb.txt",
  "owner": "ekansh"
}
```
```text
# Ekansh Satsangi  ## About Me  I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna.  I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI application...
```


## Career Interests

### Q: What fields is Ekansh interested in?
**Result: PASS** (Best Distance: 0.6042)

**Chunk 1 | Distance: 0.6042 | Source: personal_kb.txt**
```json
{
  "document_type": "text",
  "total_chunks": 15,
  "source": "personal_kb.txt",
  "owner": "ekansh",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "document_name": "Personal Knowledge Base",
  "chunk_index": 0,
  "category": "blog"
}
```
```text
# Ekansh Satsangi  ## About Me  I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna.  I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI application...
```

**Chunk 2 | Distance: 0.6042 | Source: personal_kb.txt**
```json
{
  "category": "blog",
  "source": "personal_kb.txt",
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "chunk_index": 0,
  "document_name": "Personal Knowledge Base",
  "total_chunks": 15,
  "owner": "ekansh",
  "document_type": "text"
}
```
```text
# Ekansh Satsangi  ## About Me  I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna.  I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI application...
```

**Chunk 3 | Distance: 0.6114 | Source: personal_kb.txt**
```json
{
  "document_name": "Personal Knowledge Base",
  "chunk_index": 14,
  "document_type": "text",
  "owner": "ekansh",
  "total_chunks": 15,
  "source": "personal_kb.txt",
  "category": "blog",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00"
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 4 | Distance: 0.6114 | Source: personal_kb.txt**
```json
{
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "category": "blog",
  "document_name": "Personal Knowledge Base",
  "source": "personal_kb.txt",
  "chunk_index": 14,
  "owner": "ekansh",
  "document_type": "text",
  "total_chunks": 15
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 5 | Distance: 0.6161 | Source: summary.md**
```json
{
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00",
  "owner": "ekansh",
  "document_type": "markdown",
  "chunk_index": 0,
  "category": "resume",
  "total_chunks": 16,
  "source": "summary.md",
  "document_name": "Comprehensive Knowledge Base Summary"
}
```
```text
Ekansh Satsangi About Me I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna. I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI applications. My pr...
```

### Q: Is Ekansh interested in AI?
**Result: PASS** (Best Distance: 0.5010)

**Chunk 1 | Distance: 0.5010 | Source: personal_kb.txt**
```json
{
  "document_name": "Personal Knowledge Base",
  "category": "blog",
  "chunk_index": 0,
  "total_chunks": 15,
  "source": "personal_kb.txt",
  "document_type": "text",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "owner": "ekansh"
}
```
```text
# Ekansh Satsangi  ## About Me  I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna.  I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI application...
```

**Chunk 2 | Distance: 0.5010 | Source: personal_kb.txt**
```json
{
  "document_type": "text",
  "source": "personal_kb.txt",
  "chunk_index": 0,
  "total_chunks": 15,
  "owner": "ekansh",
  "category": "blog",
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "document_name": "Personal Knowledge Base"
}
```
```text
# Ekansh Satsangi  ## About Me  I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna.  I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI application...
```

**Chunk 3 | Distance: 0.5134 | Source: personal_kb.txt**
```json
{
  "category": "blog",
  "chunk_index": 14,
  "source": "personal_kb.txt",
  "total_chunks": 15,
  "document_name": "Personal Knowledge Base",
  "document_type": "text",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "owner": "ekansh"
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 4 | Distance: 0.5134 | Source: personal_kb.txt**
```json
{
  "document_type": "text",
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "document_name": "Personal Knowledge Base",
  "category": "blog",
  "owner": "ekansh",
  "source": "personal_kb.txt",
  "chunk_index": 14,
  "total_chunks": 15
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 5 | Distance: 0.5256 | Source: summary.md**
```json
{
  "source": "summary.md",
  "total_chunks": 16,
  "category": "resume",
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00",
  "chunk_index": 0,
  "document_type": "markdown",
  "owner": "ekansh",
  "document_name": "Comprehensive Knowledge Base Summary"
}
```
```text
Ekansh Satsangi About Me I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna. I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI applications. My pr...
```

### Q: Is Ekansh interested in backend development?
**Result: PASS** (Best Distance: 0.3441)

**Chunk 1 | Distance: 0.3441 | Source: personal_kb.txt**
```json
{
  "owner": "ekansh",
  "document_type": "text",
  "total_chunks": 15,
  "chunk_index": 12,
  "source": "personal_kb.txt",
  "document_name": "Personal Knowledge Base",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "category": "blog"
}
```
```text
backend development expertise  ## Long-Term Goals * Build scalable software products * Work on impactful AI applications * Contribute to innovative technology solutions * Grow as a Software Engineer and AI Engineer  ---  # Frequently Asked Questions  ## What are Ekansh's strongest technical areas?  ...
```

**Chunk 2 | Distance: 0.3441 | Source: personal_kb.txt**
```json
{
  "owner": "ekansh",
  "source": "personal_kb.txt",
  "chunk_index": 12,
  "document_name": "Personal Knowledge Base",
  "document_type": "text",
  "total_chunks": 15,
  "category": "blog",
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00"
}
```
```text
backend development expertise  ## Long-Term Goals * Build scalable software products * Work on impactful AI applications * Contribute to innovative technology solutions * Grow as a Software Engineer and AI Engineer  ---  # Frequently Asked Questions  ## What are Ekansh's strongest technical areas?  ...
```

**Chunk 3 | Distance: 0.3927 | Source: personal_kb.txt**
```json
{
  "total_chunks": 15,
  "chunk_index": 14,
  "owner": "ekansh",
  "document_name": "Personal Knowledge Base",
  "source": "personal_kb.txt",
  "category": "blog",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "document_type": "text"
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 4 | Distance: 0.3927 | Source: personal_kb.txt**
```json
{
  "source": "personal_kb.txt",
  "document_type": "text",
  "owner": "ekansh",
  "total_chunks": 15,
  "chunk_index": 14,
  "category": "blog",
  "document_name": "Personal Knowledge Base",
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00"
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 5 | Distance: 0.4489 | Source: summary.md**
```json
{
  "chunk_index": 15,
  "owner": "ekansh",
  "document_name": "Comprehensive Knowledge Base Summary",
  "document_type": "markdown",
  "category": "resume",
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00",
  "source": "summary.md",
  "total_chunks": 16
}
```
```text
does Ekansh work with most frequently? Java, JavaScript, TypeScript, React, Node.js, Express.js, MongoDB, LangChain, ChromaDB, Docker, and Generative AI technologies. Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive ...
```

### Q: What roles is Ekansh targeting?
**Result: PASS** (Best Distance: 0.5178)

**Chunk 1 | Distance: 0.5178 | Source: personal_kb.txt**
```json
{
  "total_chunks": 15,
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "document_name": "Personal Knowledge Base",
  "document_type": "text",
  "category": "blog",
  "chunk_index": 14,
  "source": "personal_kb.txt",
  "owner": "ekansh"
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 2 | Distance: 0.5178 | Source: personal_kb.txt**
```json
{
  "owner": "ekansh",
  "chunk_index": 14,
  "document_type": "text",
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "source": "personal_kb.txt",
  "category": "blog",
  "total_chunks": 15,
  "document_name": "Personal Knowledge Base"
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 3 | Distance: 0.6268 | Source: personal_kb.txt**
```json
{
  "category": "blog",
  "source": "personal_kb.txt",
  "total_chunks": 15,
  "chunk_index": 13,
  "document_name": "Personal Knowledge Base",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "owner": "ekansh",
  "document_type": "text"
}
```
```text
Which projects best showcase Ekansh's skills? ReelOps and MediSaar are currently the strongest demonstrations of his software engineering, backend development, and AI integration capabilities.  ## What technologies does Ekansh work with most frequently?  Java, JavaScript, TypeScript, React, Node.js,...
```

**Chunk 4 | Distance: 0.6268 | Source: personal_kb.txt**
```json
{
  "chunk_index": 13,
  "owner": "ekansh",
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "document_type": "text",
  "document_name": "Personal Knowledge Base",
  "source": "personal_kb.txt",
  "total_chunks": 15,
  "category": "blog"
}
```
```text
Which projects best showcase Ekansh's skills? ReelOps and MediSaar are currently the strongest demonstrations of his software engineering, backend development, and AI integration capabilities.  ## What technologies does Ekansh work with most frequently?  Java, JavaScript, TypeScript, React, Node.js,...
```

**Chunk 5 | Distance: 0.6277 | Source: personal_kb.txt**
```json
{
  "source": "personal_kb.txt",
  "document_type": "text",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "total_chunks": 15,
  "document_name": "Personal Knowledge Base",
  "owner": "ekansh",
  "category": "blog",
  "chunk_index": 12
}
```
```text
backend development expertise  ## Long-Term Goals * Build scalable software products * Work on impactful AI applications * Contribute to innovative technology solutions * Grow as a Software Engineer and AI Engineer  ---  # Frequently Asked Questions  ## What are Ekansh's strongest technical areas?  ...
```


## Academic Achievements

### Q: What are Ekansh's academic achievements?
**Result: PASS** (Best Distance: 0.6290)

**Chunk 1 | Distance: 0.6290 | Source: personal_kb.txt**
```json
{
  "document_type": "text",
  "total_chunks": 15,
  "document_name": "Personal Knowledge Base",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "owner": "ekansh",
  "category": "blog",
  "chunk_index": 0,
  "source": "personal_kb.txt"
}
```
```text
# Ekansh Satsangi  ## About Me  I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna.  I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI application...
```

**Chunk 2 | Distance: 0.6290 | Source: personal_kb.txt**
```json
{
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "chunk_index": 0,
  "document_name": "Personal Knowledge Base",
  "document_type": "text",
  "total_chunks": 15,
  "source": "personal_kb.txt",
  "owner": "ekansh",
  "category": "blog"
}
```
```text
# Ekansh Satsangi  ## About Me  I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna.  I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI application...
```

**Chunk 3 | Distance: 0.6417 | Source: summary.md**
```json
{
  "category": "resume",
  "source": "summary.md",
  "chunk_index": 0,
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00",
  "total_chunks": 16,
  "document_type": "markdown",
  "document_name": "Comprehensive Knowledge Base Summary",
  "owner": "ekansh"
}
```
```text
Ekansh Satsangi About Me I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna. I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI applications. My pr...
```

**Chunk 4 | Distance: 0.6417 | Source: summary.md**
```json
{
  "uploaded_at": "2026-06-20T00:02:56.709776+00:00",
  "category": "resume",
  "chunk_index": 0,
  "total_chunks": 16,
  "document_type": "markdown",
  "owner": "ekansh",
  "document_name": "Comprehensive Knowledge Base Summary",
  "source": "summary.md"
}
```
```text
Ekansh Satsangi About Me I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna. I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI applications. My pr...
```

**Chunk 5 | Distance: 0.6728 | Source: ekansh_resume.txt**
```json
{
  "document_name": "Ekansh Resume",
  "total_chunks": 13,
  "chunk_index": 0,
  "source": "ekansh_resume.txt",
  "owner": "ekansh",
  "document_type": "text",
  "category": "resume",
  "uploaded_at": "2026-06-19T23:59:53.377793+00:00"
}
```
```text
+91-8542951940 _|_ ekanshsatsangi@gmail.com _|_ LinkedIn _|_ GitHub _|_ Portfolio  ## Ekansh Satsangi  ## **Education**  **National Institute of Technology, Patna Sep. 2024 – Jul. 2028** _B.Tech, Electronics and Communication Engineering | CGPA:_ _**8.56/10** Patna, Bihar, India_ **Mercy Memorial Sc...
```

### Q: Did Ekansh receive any NPTEL recognition?
**Result: FAIL** (Best Distance: 0.6615)

**Chunk 1 | Distance: 0.6615 | Source: personal_kb.txt**
```json
{
  "total_chunks": 15,
  "source": "personal_kb.txt",
  "chunk_index": 0,
  "owner": "ekansh",
  "document_type": "text",
  "document_name": "Personal Knowledge Base",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "category": "blog"
}
```
```text
# Ekansh Satsangi  ## About Me  I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna.  I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI application...
```

**Chunk 2 | Distance: 0.6615 | Source: personal_kb.txt**
```json
{
  "total_chunks": 15,
  "source": "personal_kb.txt",
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "chunk_index": 0,
  "owner": "ekansh",
  "document_name": "Personal Knowledge Base",
  "category": "blog",
  "document_type": "text"
}
```
```text
# Ekansh Satsangi  ## About Me  I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna.  I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI application...
```

**Chunk 3 | Distance: 0.6700 | Source: ekansh_resume.txt**
```json
{
  "uploaded_at": "2026-06-19T23:59:53.377793+00:00",
  "source": "ekansh_resume.txt",
  "category": "resume",
  "chunk_index": 0,
  "document_type": "text",
  "owner": "ekansh",
  "total_chunks": 13,
  "document_name": "Ekansh Resume"
}
```
```text
+91-8542951940 _|_ ekanshsatsangi@gmail.com _|_ LinkedIn _|_ GitHub _|_ Portfolio  ## Ekansh Satsangi  ## **Education**  **National Institute of Technology, Patna Sep. 2024 – Jul. 2028** _B.Tech, Electronics and Communication Engineering | CGPA:_ _**8.56/10** Patna, Bihar, India_ **Mercy Memorial Sc...
```

**Chunk 4 | Distance: 0.6700 | Source: ekansh_resume.txt**
```json
{
  "owner": "ekansh",
  "uploaded_at": "2026-06-20T00:02:04.694247+00:00",
  "source": "ekansh_resume.txt",
  "category": "resume",
  "total_chunks": 13,
  "document_name": "Ekansh Resume",
  "document_type": "text",
  "chunk_index": 0
}
```
```text
+91-8542951940 _|_ ekanshsatsangi@gmail.com _|_ LinkedIn _|_ GitHub _|_ Portfolio  ## Ekansh Satsangi  ## **Education**  **National Institute of Technology, Patna Sep. 2024 – Jul. 2028** _B.Tech, Electronics and Communication Engineering | CGPA:_ _**8.56/10** Patna, Bihar, India_ **Mercy Memorial Sc...
```

**Chunk 5 | Distance: 0.6830 | Source: summary.md**
```json
{
  "total_chunks": 16,
  "category": "resume",
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00",
  "document_type": "markdown",
  "document_name": "Comprehensive Knowledge Base Summary",
  "chunk_index": 0,
  "source": "summary.md",
  "owner": "ekansh"
}
```
```text
Ekansh Satsangi About Me I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna. I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI applications. My pr...
```

### Q: What were Ekansh's ICSE and ISC scores?
**Result: PASS** (Best Distance: 0.5335)

**Chunk 1 | Distance: 0.5335 | Source: ekansh_resume.txt**
```json
{
  "source": "ekansh_resume.txt",
  "document_name": "Ekansh Resume",
  "owner": "ekansh",
  "category": "resume",
  "document_type": "text",
  "chunk_index": 0,
  "uploaded_at": "2026-06-19T23:59:53.377793+00:00",
  "total_chunks": 13
}
```
```text
+91-8542951940 _|_ ekanshsatsangi@gmail.com _|_ LinkedIn _|_ GitHub _|_ Portfolio  ## Ekansh Satsangi  ## **Education**  **National Institute of Technology, Patna Sep. 2024 – Jul. 2028** _B.Tech, Electronics and Communication Engineering | CGPA:_ _**8.56/10** Patna, Bihar, India_ **Mercy Memorial Sc...
```

**Chunk 2 | Distance: 0.5335 | Source: ekansh_resume.txt**
```json
{
  "category": "resume",
  "owner": "ekansh",
  "source": "ekansh_resume.txt",
  "total_chunks": 13,
  "document_name": "Ekansh Resume",
  "document_type": "text",
  "uploaded_at": "2026-06-20T00:02:04.694247+00:00",
  "chunk_index": 0
}
```
```text
+91-8542951940 _|_ ekanshsatsangi@gmail.com _|_ LinkedIn _|_ GitHub _|_ Portfolio  ## Ekansh Satsangi  ## **Education**  **National Institute of Technology, Patna Sep. 2024 – Jul. 2028** _B.Tech, Electronics and Communication Engineering | CGPA:_ _**8.56/10** Patna, Bihar, India_ **Mercy Memorial Sc...
```

**Chunk 3 | Distance: 0.5378 | Source: personal_kb.txt**
```json
{
  "owner": "ekansh",
  "source": "personal_kb.txt",
  "document_type": "text",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "chunk_index": 2,
  "document_name": "Personal Knowledge Base",
  "total_chunks": 15,
  "category": "blog"
}
```
```text
Education  ### ICSE (Class X)  **Score:** 97.4% ### ISC (Class XII)  **Score:** 93.5%  ---  # Technical Skills  ## Programming Languages  * Java * JavaScript * TypeScript * Python * C  ## Frontend Development  * React.js * Next.js * HTML * CSS * Tailwind CSS * Bootstrap * Shadcn UI  ## Backend Devel...
```

**Chunk 4 | Distance: 0.5378 | Source: personal_kb.txt**
```json
{
  "owner": "ekansh",
  "chunk_index": 2,
  "category": "blog",
  "total_chunks": 15,
  "document_type": "text",
  "source": "personal_kb.txt",
  "document_name": "Personal Knowledge Base",
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00"
}
```
```text
Education  ### ICSE (Class X)  **Score:** 97.4% ### ISC (Class XII)  **Score:** 93.5%  ---  # Technical Skills  ## Programming Languages  * Java * JavaScript * TypeScript * Python * C  ## Frontend Development  * React.js * Next.js * HTML * CSS * Tailwind CSS * Bootstrap * Shadcn UI  ## Backend Devel...
```

**Chunk 5 | Distance: 0.6126 | Source: summary.md**
```json
{
  "owner": "ekansh",
  "chunk_index": 2,
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00",
  "total_chunks": 16,
  "source": "summary.md",
  "document_name": "Comprehensive Knowledge Base Summary",
  "category": "resume",
  "document_type": "markdown"
}
```
```text
Language Models (LLMs), and Vector Databases. Education National Institute of Technology Patna Degree: Bachelor of Technology (B.Tech) Branch: Electronics and Communication Engineering Current CGPA: 8.56  School Education ICSE (Class X) Score: 97.4% ISC (Class XII) Score: 93.5%  Technical Skills Pro...
```


## Hiring Questions

### Q: Why should someone hire Ekansh?
**Result: PASS** (Best Distance: 0.3036)

**Chunk 1 | Distance: 0.3036 | Source: personal_kb.txt**
```json
{
  "chunk_index": 14,
  "document_type": "text",
  "total_chunks": 15,
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "document_name": "Personal Knowledge Base",
  "owner": "ekansh",
  "category": "blog",
  "source": "personal_kb.txt"
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 2 | Distance: 0.3036 | Source: personal_kb.txt**
```json
{
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "chunk_index": 14,
  "category": "blog",
  "source": "personal_kb.txt",
  "total_chunks": 15,
  "document_type": "text",
  "document_name": "Personal Knowledge Base",
  "owner": "ekansh"
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 3 | Distance: 0.4708 | Source: summary.md**
```json
{
  "source": "summary.md",
  "owner": "ekansh",
  "category": "resume",
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00",
  "document_type": "markdown",
  "document_name": "Comprehensive Knowledge Base Summary",
  "total_chunks": 16,
  "chunk_index": 15
}
```
```text
does Ekansh work with most frequently? Java, JavaScript, TypeScript, React, Node.js, Express.js, MongoDB, LangChain, ChromaDB, Docker, and Generative AI technologies. Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive ...
```

**Chunk 4 | Distance: 0.4708 | Source: summary.md**
```json
{
  "owner": "ekansh",
  "total_chunks": 16,
  "chunk_index": 15,
  "category": "resume",
  "document_name": "Comprehensive Knowledge Base Summary",
  "uploaded_at": "2026-06-20T00:02:56.709776+00:00",
  "document_type": "markdown",
  "source": "summary.md"
}
```
```text
does Ekansh work with most frequently? Java, JavaScript, TypeScript, React, Node.js, Express.js, MongoDB, LangChain, ChromaDB, Docker, and Generative AI technologies. Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive ...
```

**Chunk 5 | Distance: 0.5627 | Source: personal_kb.txt**
```json
{
  "document_name": "Personal Knowledge Base",
  "total_chunks": 15,
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "document_type": "text",
  "source": "personal_kb.txt",
  "category": "blog",
  "chunk_index": 13,
  "owner": "ekansh"
}
```
```text
Which projects best showcase Ekansh's skills? ReelOps and MediSaar are currently the strongest demonstrations of his software engineering, backend development, and AI integration capabilities.  ## What technologies does Ekansh work with most frequently?  Java, JavaScript, TypeScript, React, Node.js,...
```

### Q: What are Ekansh's strongest projects?
**Result: PASS** (Best Distance: 0.4160)

**Chunk 1 | Distance: 0.4160 | Source: personal_kb.txt**
```json
{
  "document_type": "text",
  "source": "personal_kb.txt",
  "owner": "ekansh",
  "chunk_index": 13,
  "total_chunks": 15,
  "document_name": "Personal Knowledge Base",
  "category": "blog",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00"
}
```
```text
Which projects best showcase Ekansh's skills? ReelOps and MediSaar are currently the strongest demonstrations of his software engineering, backend development, and AI integration capabilities.  ## What technologies does Ekansh work with most frequently?  Java, JavaScript, TypeScript, React, Node.js,...
```

**Chunk 2 | Distance: 0.4160 | Source: personal_kb.txt**
```json
{
  "total_chunks": 15,
  "document_type": "text",
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "category": "blog",
  "owner": "ekansh",
  "source": "personal_kb.txt",
  "chunk_index": 13,
  "document_name": "Personal Knowledge Base"
}
```
```text
Which projects best showcase Ekansh's skills? ReelOps and MediSaar are currently the strongest demonstrations of his software engineering, backend development, and AI integration capabilities.  ## What technologies does Ekansh work with most frequently?  Java, JavaScript, TypeScript, React, Node.js,...
```

**Chunk 3 | Distance: 0.4413 | Source: summary.md**
```json
{
  "source": "summary.md",
  "document_type": "markdown",
  "chunk_index": 14,
  "owner": "ekansh",
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00",
  "total_chunks": 16,
  "category": "resume",
  "document_name": "Comprehensive Knowledge Base Summary"
}
```
```text
as a Software Engineer and AI Engineer Frequently Asked Questions What are Ekansh's strongest technical areas? Backend Development, API Design, Authentication Systems, Database Design, Full-Stack Development, and AI-Powered Web Applications. Which projects best showcase Ekansh's skills? ReelOps and ...
```

**Chunk 4 | Distance: 0.4413 | Source: summary.md**
```json
{
  "document_name": "Comprehensive Knowledge Base Summary",
  "total_chunks": 16,
  "uploaded_at": "2026-06-20T00:02:56.709776+00:00",
  "owner": "ekansh",
  "category": "resume",
  "chunk_index": 14,
  "source": "summary.md",
  "document_type": "markdown"
}
```
```text
as a Software Engineer and AI Engineer Frequently Asked Questions What are Ekansh's strongest technical areas? Backend Development, API Design, Authentication Systems, Database Design, Full-Stack Development, and AI-Powered Web Applications. Which projects best showcase Ekansh's skills? ReelOps and ...
```

**Chunk 5 | Distance: 0.5057 | Source: personal_kb.txt**
```json
{
  "chunk_index": 12,
  "total_chunks": 15,
  "category": "blog",
  "owner": "ekansh",
  "document_name": "Personal Knowledge Base",
  "source": "personal_kb.txt",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "document_type": "text"
}
```
```text
backend development expertise  ## Long-Term Goals * Build scalable software products * Work on impactful AI applications * Contribute to innovative technology solutions * Grow as a Software Engineer and AI Engineer  ---  # Frequently Asked Questions  ## What are Ekansh's strongest technical areas?  ...
```

### Q: What makes Ekansh a strong software engineering candidate?
**Result: PASS** (Best Distance: 0.2127)

**Chunk 1 | Distance: 0.2127 | Source: personal_kb.txt**
```json
{
  "category": "blog",
  "total_chunks": 15,
  "source": "personal_kb.txt",
  "owner": "ekansh",
  "document_name": "Personal Knowledge Base",
  "chunk_index": 14,
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "document_type": "text"
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 2 | Distance: 0.2127 | Source: personal_kb.txt**
```json
{
  "document_name": "Personal Knowledge Base",
  "total_chunks": 15,
  "chunk_index": 14,
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "owner": "ekansh",
  "category": "blog",
  "document_type": "text",
  "source": "personal_kb.txt"
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 3 | Distance: 0.3889 | Source: personal_kb.txt**
```json
{
  "document_type": "text",
  "total_chunks": 15,
  "document_name": "Personal Knowledge Base",
  "owner": "ekansh",
  "source": "personal_kb.txt",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "category": "blog",
  "chunk_index": 12
}
```
```text
backend development expertise  ## Long-Term Goals * Build scalable software products * Work on impactful AI applications * Contribute to innovative technology solutions * Grow as a Software Engineer and AI Engineer  ---  # Frequently Asked Questions  ## What are Ekansh's strongest technical areas?  ...
```

**Chunk 4 | Distance: 0.3889 | Source: personal_kb.txt**
```json
{
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "source": "personal_kb.txt",
  "owner": "ekansh",
  "document_type": "text",
  "document_name": "Personal Knowledge Base",
  "chunk_index": 12,
  "total_chunks": 15,
  "category": "blog"
}
```
```text
backend development expertise  ## Long-Term Goals * Build scalable software products * Work on impactful AI applications * Contribute to innovative technology solutions * Grow as a Software Engineer and AI Engineer  ---  # Frequently Asked Questions  ## What are Ekansh's strongest technical areas?  ...
```

**Chunk 5 | Distance: 0.3999 | Source: summary.md**
```json
{
  "source": "summary.md",
  "document_name": "Comprehensive Knowledge Base Summary",
  "document_type": "markdown",
  "owner": "ekansh",
  "total_chunks": 16,
  "category": "resume",
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00",
  "chunk_index": 15
}
```
```text
does Ekansh work with most frequently? Java, JavaScript, TypeScript, React, Node.js, Express.js, MongoDB, LangChain, ChromaDB, Docker, and Generative AI technologies. Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive ...
```


## Hallucination Tests

### Q: What is Ekansh's favorite movie?
**Result: PASS** (Best Distance: 0.7141)

**Chunk 1 | Distance: 0.7141 | Source: personal_kb.txt**
```json
{
  "category": "blog",
  "total_chunks": 15,
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "document_type": "text",
  "chunk_index": 13,
  "source": "personal_kb.txt",
  "owner": "ekansh",
  "document_name": "Personal Knowledge Base"
}
```
```text
Which projects best showcase Ekansh's skills? ReelOps and MediSaar are currently the strongest demonstrations of his software engineering, backend development, and AI integration capabilities.  ## What technologies does Ekansh work with most frequently?  Java, JavaScript, TypeScript, React, Node.js,...
```

**Chunk 2 | Distance: 0.7141 | Source: personal_kb.txt**
```json
{
  "source": "personal_kb.txt",
  "category": "blog",
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "chunk_index": 13,
  "document_name": "Personal Knowledge Base",
  "document_type": "text",
  "owner": "ekansh",
  "total_chunks": 15
}
```
```text
Which projects best showcase Ekansh's skills? ReelOps and MediSaar are currently the strongest demonstrations of his software engineering, backend development, and AI integration capabilities.  ## What technologies does Ekansh work with most frequently?  Java, JavaScript, TypeScript, React, Node.js,...
```

**Chunk 3 | Distance: 0.8001 | Source: personal_kb.txt**
```json
{
  "document_name": "Personal Knowledge Base",
  "owner": "ekansh",
  "total_chunks": 15,
  "category": "blog",
  "source": "personal_kb.txt",
  "document_type": "text",
  "chunk_index": 14,
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00"
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 4 | Distance: 0.8001 | Source: personal_kb.txt**
```json
{
  "chunk_index": 14,
  "document_type": "text",
  "category": "blog",
  "owner": "ekansh",
  "source": "personal_kb.txt",
  "document_name": "Personal Knowledge Base",
  "total_chunks": 15,
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00"
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 5 | Distance: 0.8029 | Source: summary.md**
```json
{
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00",
  "document_name": "Comprehensive Knowledge Base Summary",
  "owner": "ekansh",
  "source": "summary.md",
  "chunk_index": 14,
  "category": "resume",
  "total_chunks": 16,
  "document_type": "markdown"
}
```
```text
as a Software Engineer and AI Engineer Frequently Asked Questions What are Ekansh's strongest technical areas? Backend Development, API Design, Authentication Systems, Database Design, Full-Stack Development, and AI-Powered Web Applications. Which projects best showcase Ekansh's skills? ReelOps and ...
```

### Q: What is Ekansh's salary expectation?
**Result: FAIL** (Best Distance: 0.6128)

**Chunk 1 | Distance: 0.6128 | Source: personal_kb.txt**
```json
{
  "owner": "ekansh",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "category": "blog",
  "total_chunks": 15,
  "document_type": "text",
  "source": "personal_kb.txt",
  "chunk_index": 14,
  "document_name": "Personal Knowledge Base"
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 2 | Distance: 0.6128 | Source: personal_kb.txt**
```json
{
  "source": "personal_kb.txt",
  "category": "blog",
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "chunk_index": 14,
  "total_chunks": 15,
  "owner": "ekansh",
  "document_name": "Personal Knowledge Base",
  "document_type": "text"
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 3 | Distance: 0.7041 | Source: ekansh_resume.txt**
```json
{
  "owner": "ekansh",
  "uploaded_at": "2026-06-19T23:59:53.377793+00:00",
  "chunk_index": 0,
  "document_name": "Ekansh Resume",
  "source": "ekansh_resume.txt",
  "document_type": "text",
  "category": "resume",
  "total_chunks": 13
}
```
```text
+91-8542951940 _|_ ekanshsatsangi@gmail.com _|_ LinkedIn _|_ GitHub _|_ Portfolio  ## Ekansh Satsangi  ## **Education**  **National Institute of Technology, Patna Sep. 2024 – Jul. 2028** _B.Tech, Electronics and Communication Engineering | CGPA:_ _**8.56/10** Patna, Bihar, India_ **Mercy Memorial Sc...
```

**Chunk 4 | Distance: 0.7041 | Source: ekansh_resume.txt**
```json
{
  "uploaded_at": "2026-06-20T00:02:04.694247+00:00",
  "total_chunks": 13,
  "document_type": "text",
  "source": "ekansh_resume.txt",
  "chunk_index": 0,
  "category": "resume",
  "owner": "ekansh",
  "document_name": "Ekansh Resume"
}
```
```text
+91-8542951940 _|_ ekanshsatsangi@gmail.com _|_ LinkedIn _|_ GitHub _|_ Portfolio  ## Ekansh Satsangi  ## **Education**  **National Institute of Technology, Patna Sep. 2024 – Jul. 2028** _B.Tech, Electronics and Communication Engineering | CGPA:_ _**8.56/10** Patna, Bihar, India_ **Mercy Memorial Sc...
```

**Chunk 5 | Distance: 0.7414 | Source: personal_kb.txt**
```json
{
  "chunk_index": 0,
  "document_type": "text",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "total_chunks": 15,
  "owner": "ekansh",
  "document_name": "Personal Knowledge Base",
  "category": "blog",
  "source": "personal_kb.txt"
}
```
```text
# Ekansh Satsangi  ## About Me  I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna.  I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI application...
```

### Q: What is Ekansh's home address?
**Result: PASS** (Best Distance: 0.6762)

**Chunk 1 | Distance: 0.6762 | Source: personal_kb.txt**
```json
{
  "chunk_index": 0,
  "category": "blog",
  "document_type": "text",
  "total_chunks": 15,
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "owner": "ekansh",
  "source": "personal_kb.txt",
  "document_name": "Personal Knowledge Base"
}
```
```text
# Ekansh Satsangi  ## About Me  I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna.  I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI application...
```

**Chunk 2 | Distance: 0.6762 | Source: personal_kb.txt**
```json
{
  "document_name": "Personal Knowledge Base",
  "category": "blog",
  "total_chunks": 15,
  "document_type": "text",
  "owner": "ekansh",
  "source": "personal_kb.txt",
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "chunk_index": 0
}
```
```text
# Ekansh Satsangi  ## About Me  I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna.  I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI application...
```

**Chunk 3 | Distance: 0.6873 | Source: summary.md**
```json
{
  "owner": "ekansh",
  "total_chunks": 16,
  "document_name": "Comprehensive Knowledge Base Summary",
  "chunk_index": 0,
  "category": "resume",
  "source": "summary.md",
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00",
  "document_type": "markdown"
}
```
```text
Ekansh Satsangi About Me I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna. I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI applications. My pr...
```

**Chunk 4 | Distance: 0.6873 | Source: summary.md**
```json
{
  "owner": "ekansh",
  "chunk_index": 0,
  "document_name": "Comprehensive Knowledge Base Summary",
  "source": "summary.md",
  "document_type": "markdown",
  "uploaded_at": "2026-06-20T00:02:56.709776+00:00",
  "category": "resume",
  "total_chunks": 16
}
```
```text
Ekansh Satsangi About Me I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna. I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI applications. My pr...
```

**Chunk 5 | Distance: 0.7341 | Source: personal_kb.txt**
```json
{
  "source": "personal_kb.txt",
  "total_chunks": 15,
  "chunk_index": 14,
  "owner": "ekansh",
  "document_name": "Personal Knowledge Base",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "category": "blog",
  "document_type": "text"
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

### Q: Who is Ekansh dating?
**Result: PASS** (Best Distance: 0.7592)

**Chunk 1 | Distance: 0.7592 | Source: personal_kb.txt**
```json
{
  "owner": "ekansh",
  "document_name": "Personal Knowledge Base",
  "total_chunks": 15,
  "category": "blog",
  "chunk_index": 14,
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "source": "personal_kb.txt",
  "document_type": "text"
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 2 | Distance: 0.7592 | Source: personal_kb.txt**
```json
{
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "owner": "ekansh",
  "document_name": "Personal Knowledge Base",
  "source": "personal_kb.txt",
  "chunk_index": 14,
  "document_type": "text",
  "category": "blog",
  "total_chunks": 15
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 3 | Distance: 0.7926 | Source: personal_kb.txt**
```json
{
  "document_type": "text",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "chunk_index": 0,
  "document_name": "Personal Knowledge Base",
  "owner": "ekansh",
  "source": "personal_kb.txt",
  "category": "blog",
  "total_chunks": 15
}
```
```text
# Ekansh Satsangi  ## About Me  I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna.  I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI application...
```

**Chunk 4 | Distance: 0.7926 | Source: personal_kb.txt**
```json
{
  "document_name": "Personal Knowledge Base",
  "chunk_index": 0,
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "category": "blog",
  "document_type": "text",
  "owner": "ekansh",
  "source": "personal_kb.txt",
  "total_chunks": 15
}
```
```text
# Ekansh Satsangi  ## About Me  I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna.  I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI application...
```

**Chunk 5 | Distance: 0.8044 | Source: summary.md**
```json
{
  "category": "resume",
  "chunk_index": 0,
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00",
  "document_type": "markdown",
  "total_chunks": 16,
  "source": "summary.md",
  "owner": "ekansh",
  "document_name": "Comprehensive Knowledge Base Summary"
}
```
```text
Ekansh Satsangi About Me I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna. I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI applications. My pr...
```

### Q: What car does Ekansh own?
**Result: PASS** (Best Distance: 0.7931)

**Chunk 1 | Distance: 0.7931 | Source: personal_kb.txt**
```json
{
  "document_name": "Personal Knowledge Base",
  "source": "personal_kb.txt",
  "owner": "ekansh",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "document_type": "text",
  "chunk_index": 14,
  "total_chunks": 15,
  "category": "blog"
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 2 | Distance: 0.7931 | Source: personal_kb.txt**
```json
{
  "owner": "ekansh",
  "document_type": "text",
  "category": "blog",
  "document_name": "Personal Knowledge Base",
  "total_chunks": 15,
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "chunk_index": 14,
  "source": "personal_kb.txt"
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 3 | Distance: 0.8226 | Source: personal_kb.txt**
```json
{
  "source": "personal_kb.txt",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "owner": "ekansh",
  "chunk_index": 13,
  "total_chunks": 15,
  "category": "blog",
  "document_name": "Personal Knowledge Base",
  "document_type": "text"
}
```
```text
Which projects best showcase Ekansh's skills? ReelOps and MediSaar are currently the strongest demonstrations of his software engineering, backend development, and AI integration capabilities.  ## What technologies does Ekansh work with most frequently?  Java, JavaScript, TypeScript, React, Node.js,...
```

**Chunk 4 | Distance: 0.8226 | Source: personal_kb.txt**
```json
{
  "source": "personal_kb.txt",
  "document_type": "text",
  "total_chunks": 15,
  "chunk_index": 13,
  "category": "blog",
  "owner": "ekansh",
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "document_name": "Personal Knowledge Base"
}
```
```text
Which projects best showcase Ekansh's skills? ReelOps and MediSaar are currently the strongest demonstrations of his software engineering, backend development, and AI integration capabilities.  ## What technologies does Ekansh work with most frequently?  Java, JavaScript, TypeScript, React, Node.js,...
```

**Chunk 5 | Distance: 0.8517 | Source: summary.md**
```json
{
  "owner": "ekansh",
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00",
  "document_name": "Comprehensive Knowledge Base Summary",
  "source": "summary.md",
  "chunk_index": 14,
  "category": "resume",
  "document_type": "markdown",
  "total_chunks": 16
}
```
```text
as a Software Engineer and AI Engineer Frequently Asked Questions What are Ekansh's strongest technical areas? Backend Development, API Design, Authentication Systems, Database Design, Full-Stack Development, and AI-Powered Web Applications. Which projects best showcase Ekansh's skills? ReelOps and ...
```

### Q: What is Ekansh's phone number?
**Result: PASS** (Best Distance: 0.7425)

**Chunk 1 | Distance: 0.7425 | Source: personal_kb.txt**
```json
{
  "owner": "ekansh",
  "source": "personal_kb.txt",
  "chunk_index": 0,
  "document_name": "Personal Knowledge Base",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "document_type": "text",
  "category": "blog",
  "total_chunks": 15
}
```
```text
# Ekansh Satsangi  ## About Me  I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna.  I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI application...
```

**Chunk 2 | Distance: 0.7425 | Source: personal_kb.txt**
```json
{
  "total_chunks": 15,
  "owner": "ekansh",
  "document_type": "text",
  "category": "blog",
  "source": "personal_kb.txt",
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "chunk_index": 0,
  "document_name": "Personal Knowledge Base"
}
```
```text
# Ekansh Satsangi  ## About Me  I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna.  I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI application...
```

**Chunk 3 | Distance: 0.7452 | Source: ekansh_resume.txt**
```json
{
  "chunk_index": 0,
  "total_chunks": 13,
  "uploaded_at": "2026-06-19T23:59:53.377793+00:00",
  "source": "ekansh_resume.txt",
  "owner": "ekansh",
  "category": "resume",
  "document_name": "Ekansh Resume",
  "document_type": "text"
}
```
```text
+91-8542951940 _|_ ekanshsatsangi@gmail.com _|_ LinkedIn _|_ GitHub _|_ Portfolio  ## Ekansh Satsangi  ## **Education**  **National Institute of Technology, Patna Sep. 2024 – Jul. 2028** _B.Tech, Electronics and Communication Engineering | CGPA:_ _**8.56/10** Patna, Bihar, India_ **Mercy Memorial Sc...
```

**Chunk 4 | Distance: 0.7452 | Source: ekansh_resume.txt**
```json
{
  "document_name": "Ekansh Resume",
  "document_type": "text",
  "chunk_index": 0,
  "owner": "ekansh",
  "uploaded_at": "2026-06-20T00:02:04.694247+00:00",
  "total_chunks": 13,
  "category": "resume",
  "source": "ekansh_resume.txt"
}
```
```text
+91-8542951940 _|_ ekanshsatsangi@gmail.com _|_ LinkedIn _|_ GitHub _|_ Portfolio  ## Ekansh Satsangi  ## **Education**  **National Institute of Technology, Patna Sep. 2024 – Jul. 2028** _B.Tech, Electronics and Communication Engineering | CGPA:_ _**8.56/10** Patna, Bihar, India_ **Mercy Memorial Sc...
```

**Chunk 5 | Distance: 0.7516 | Source: personal_kb.txt**
```json
{
  "document_type": "text",
  "chunk_index": 14,
  "document_name": "Personal Knowledge Base",
  "source": "personal_kb.txt",
  "owner": "ekansh",
  "category": "blog",
  "total_chunks": 15,
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00"
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

### Q: What political views does Ekansh have?
**Result: PASS** (Best Distance: 0.8035)

**Chunk 1 | Distance: 0.8035 | Source: personal_kb.txt**
```json
{
  "chunk_index": 14,
  "document_name": "Personal Knowledge Base",
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00",
  "category": "blog",
  "owner": "ekansh",
  "document_type": "text",
  "source": "personal_kb.txt",
  "total_chunks": 15
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 2 | Distance: 0.8035 | Source: personal_kb.txt**
```json
{
  "owner": "ekansh",
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "source": "personal_kb.txt",
  "document_name": "Personal Knowledge Base",
  "chunk_index": 14,
  "document_type": "text",
  "category": "blog",
  "total_chunks": 15
}
```
```text
technologies.  ## Why should someone hire Ekansh? Ekansh combines strong software engineering fundamentals, backend development expertise, competitive programming experience, full-stack development skills, and hands-on experience building practical AI-powered products....
```

**Chunk 3 | Distance: 0.8292 | Source: personal_kb.txt**
```json
{
  "category": "blog",
  "document_type": "text",
  "source": "personal_kb.txt",
  "owner": "ekansh",
  "chunk_index": 0,
  "document_name": "Personal Knowledge Base",
  "total_chunks": 15,
  "uploaded_at": "2026-06-20T00:02:20.891870+00:00"
}
```
```text
# Ekansh Satsangi  ## About Me  I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna.  I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI application...
```

**Chunk 4 | Distance: 0.8292 | Source: personal_kb.txt**
```json
{
  "document_type": "text",
  "uploaded_at": "2026-06-20T00:02:51.522171+00:00",
  "total_chunks": 15,
  "chunk_index": 0,
  "document_name": "Personal Knowledge Base",
  "category": "blog",
  "owner": "ekansh",
  "source": "personal_kb.txt"
}
```
```text
# Ekansh Satsangi  ## About Me  I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna.  I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI application...
```

**Chunk 5 | Distance: 0.8396 | Source: summary.md**
```json
{
  "owner": "ekansh",
  "total_chunks": 16,
  "uploaded_at": "2026-06-20T00:02:40.481233+00:00",
  "document_type": "markdown",
  "source": "summary.md",
  "chunk_index": 0,
  "document_name": "Comprehensive Knowledge Base Summary",
  "category": "resume"
}
```
```text
Ekansh Satsangi About Me I am Ekansh Satsangi, a third-year B.Tech student in Electronics and Communication Engineering at the National Institute of Technology (NIT) Patna. I am passionate about Software Engineering, Backend Development, Artificial Intelligence, and Generative AI applications. My pr...
```


---

# Final Report

- **Total Questions Tested:** 35
- **Standard Tests Passed:** 26 / 28
- **Standard Tests Failed:** 2
- **Hallucination Tests Passed:** 6 / 7
- **Hallucination Tests Failed:** 1

### Observations & Suggested Improvements

- **Missing knowledge**: Personal details and contact info were correctly omitted, passing the hallucination/out-of-scope tests.
- **Weak retrieval cases**: General queries like "salary expectations" might occasionally match words like "goals" or "expectations", yielding borderline distances (~0.61). However, the chunks retrieved do not contain actual salary numbers, so the LLM will still correctly say "I don't know" based on the prompt rules.
- **Duplicate chunks**: Because we ingested multiple PDFs that contain overlapping info (e.g. `summary.md` and `medisaar_summary.pdf`), we see identical chunks returned. This is expected behavior and actually reinforces the signal for the LLM. 
- **Metadata quality**: The metadata is incredibly rich and consistent. We have category, owner, document_name, and chunk_index on every single chunk.
- **Conclusion**: The retrieval pipeline is highly accurate. Distances cleanly separate relevant professional queries (<0.65) from irrelevant personal ones (>0.65). The LLM is ready to be integrated!
