# 📚 SmartStudy — Textbook & Exam Question Mapper

SmartStudy helps students **study smarter, not harder** by automatically mapping exam-style questions to the exact textbook passages they need to review.  
Upload your textbooks and past exam papers, and the system finds, ranks, and organizes related textbook questions/passages from **easy → hard**.

---

## ✨ Features
- 📂 **Upload multiple textbooks** (PDF, EPUB, TXT; scanned PDFs supported via OCR).
- 📝 **Upload past exam question papers** — questions are extracted and indexed.
- 🔍 **Automated matching** — for each exam question, the system finds the most relevant textbook passages/questions.
- 📊 **Difficulty ranking** — results are ordered from easy to hard, using a mix of heuristics + LLM judgment.
- 📖 **Source transparency** — each match shows textbook title, chapter/page, and snippet.
- 👍 **Feedback loop** — mark results as helpful / not helpful to improve quality.

---

## 🚀 Tech Stack
- **Frontend**: [Next.js](https://nextjs.org/) (React) for upload + results UI.
- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) (Python) for API endpoints.
- **Storage**: Local filesystem (MVP) — S3/Cloud storage later.
- **Parsing & OCR**: `pypdf`, `pdfminer.six`, `pytesseract` for text extraction.
- **Embeddings**: [OpenAI Embeddings](https://platform.openai.com/docs/guides/embeddings) or [`sentence-transformers`](https://www.sbert.net/) for local.
- **Vector DB**: [LanceDB](https://lancedb.com/) for storing chunks & question embeddings.
- **LLM**: OpenAI GPT-4o (default) or local models (Llama2/vLLM) for offline use.

---

## 📂 Project TODO List
# ✅ 14-Day MVP Timetable (no web search / no auto-download)

| Done | Day | Goal | Tasks (exact, actionable) | Deliverable / Acceptance criteria |
|:---:|---:|---|---|---|
| - [x] | **Day 1** | Project setup & plan | - Create GitHub repo and branches (main, dev).<br>- Update README with MVP scope (user uploads ≥3 textbooks + question papers; LanceDB; LLM mapping & ranking).<br>- Choose stack: Next.js (frontend), FastAPI (backend), Python ingestion, LanceDB, OpenAI or local embeddings/LLM. | Repo + README with clear scope & tech stack; branches created. |
| - [ ] | **Day 2** | Frontend upload UI | - Scaffold Next.js app.<br>- Build upload page: allow multiple file selection, labeled buckets for **Textbooks** and **Question Papers**.<br>- Client validate filetypes (pdf/epub/txt) and show progress bar. | Upload page working and sending files to backend (even if backend stub). |
| - [ ] | **Day 3** | Backend upload/storage | - Implement FastAPI upload endpoints (multipart).<br>- Save files to server storage (local) and record session/user id grouping.<br>- Return metadata (file id, filename, type). | Files persist on server; endpoint returns metadata; frontend lists uploaded files per session. |
| - [ ] | **Day 4** | PDF/Text parsing & OCR | - Implement document parser: `pypdf`/`pdfminer.six` for PDFs; `pytesseract` fallback for scanned PDFs; EPUB/TXT parser.<br>- Normalize text (remove headers/footers; whitespace).<br>- Implement chunker (500–800 tokens, 100–150 token overlap). | `ingest/parse_documents.py` that turns uploaded files into normalized JSONL chunks. |
| - [ ] | **Day 5** | Embeddings & LanceDB ingestion | - Choose embeddings (OpenAI or `sentence-transformers`).<br>- Generate embeddings for chunks and store in LanceDB with metadata schema: `{book_title, book_id, chapter, source_filename, chunk_text, offset}`.<br>- Add simple script to inspect LanceDB contents. | LanceDB populated for at least one uploaded textbook; nearest-neighbor query returns meaningful chunks. |
| - [ ] | **Day 6** | Question paper parsing & indexing | - Parse question PDFs into discrete questions (heuristics: numbered lists, blank lines).<br>- Normalize questions and embed; store in LanceDB (type: question).<br>- Add backend API to list parsed questions for a session. | Question embeddings stored; API lists parsed questions; quick NN test works. |
| - [ ] | **Day 7** | Ensure ≥3 textbooks in DB (user flow) | - Implement a UI/flow that requires or highlights "You need at least 3 textbooks" and prevents mapping until met.<br>- Optionally add an “Import sample textbooks” button (local sample files) for testing/demo if the user doesn’t have 3 files ready. | UI blocks mapping until 3 textbooks present; at least one test session with 3 books in DB (either user uploads or samples). |
| - [ ] | **Day 8** | Retrieval pipeline & basic matching | - Build retrieval function: for a given exam question, query LanceDB for top-N chunks across textbooks.<br>- Return candidate chunks with metadata and raw similarity scores. | Endpoint `/retrieve_candidates` returns top-N chunks for a question with metadata. |
| - [ ] | **Day 9** | LLM mapping: turn chunks → textbook matches | - Create LLM prompt template that provides exam question + retrieved chunks and asks the model to extract textbook questions/passages that match, with short justification.<br>- Implement backend endpoint `/match_question` that returns mapped textbook snippets + justification. | `/match_question` returns mapped textbook snippets with justifications for test questions. |
| - [ ] | **Day 10** | Difficulty scoring & ranking pipeline | - Implement difficulty scoring using heuristics + LLM scoring:<br>  • Heuristics: keywords (`prove/derive/explain`), length, Bloom’s taxonomy keywords.<br>  • LLM: ask for 1–5 difficulty score with one-line rationale.<br>- Aggregate similarity + LLM difficulty + heuristics into final ranking (Easy→Hard). | Each mapping result includes `similarity`, `difficulty_score (1–5)`, `difficulty_label`, and final rank. |
| - [ ] | **Day 11** | Frontend results UI & feedback | - Build results page listing each exam question and ranked textbook matches (Easy→Hard).<br>- Show source book, chapter/page, snippet, similarity, difficulty, and a link to the uploaded source file (or viewer).<br>- Add feedback buttons (helpful / not helpful) that POST to an endpoint. | Results UI shows ranked matches per question; feedback stored. |
| - [ ] | **Day 12** | End-to-end testing & error handling | - Run end-to-end tests with multiple real textbook+paper sets (including scanned PDFs).<br>- Add robust error handling and retries (OCR failures, embedding API rate limits).<br>- Add logging for pipeline steps. | End-to-end tests pass for several cases; errors are handled gracefully and logged. |
| - [ ] | **Day 13** | Performance tuning & small features | - Tune chunk sizes/overlap and retrieval `k` if matches are noisy.<br>- Add caching for repeated questions and re-use embeddings.<br>- Add session persistence and basic rate limiting for uploads. | Faster, more accurate retrieval; caching reduces duplicate compute. |
| - [ ] | **Day 14** | Deploy MVP & docs | - Deploy backend (Render, Heroku, or a VM) and frontend (Vercel).<br>- Add deployment README, runbook, and a short demo script: how to upload 3 textbooks + exam paper and run mapping.<br>- Collect quick tester feedback (2–3 users) and list next improvements. | Deployed MVP reachable; README + demo script available; at least one demo run completed successfully. |

