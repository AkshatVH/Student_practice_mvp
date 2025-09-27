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

## 📂 Project Structure (MVP)

