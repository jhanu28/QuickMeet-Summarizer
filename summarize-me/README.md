# 🤖 QuickMeet: AI for Faster Meeting Insights

![Banner](images/upload.png) <!-- Replace with an actual banner if available -->

**QuickMeet** is a smart AI-based web application that transforms long, cluttered meeting recordings into clear summaries, structured action items, and engaging avatar-based video recaps. Built using AWS, HuggingFace Transformers, and modern web tech, it is a productivity booster for individuals and teams relying on virtual collaboration.

---

## ✨ Features

- 🎙️ **Speech-to-Text** using AWS Transcribe
- 🧠 **Abstractive Summarization** with HuggingFace BART models
- ✅ **Action Item Extraction** using Regex + NLP
- 🔍 **Semantic Search** powered by Sentence Transformers
- 📄 **Export Options** – Download results as PDF or PPT
- ✉️ **Send via Email** – AWS SES Integration
- 🎥 **AI Avatar Video Generation** via HeyGen API

---

## 🖼️ Screenshots

| Upload Page | Transcript Viewer |
|-------------|-------------------|
| ![Upload](images/upload.png) | ![Transcript](images/transcript.png) |

| Summary & Actions | Semantic Search |
|-------------------|-----------------|
| ![Summary](images/summary.png) | ![Search](images/search.png) |

| Export Options | Email Sent |
|----------------|------------|
| ![Export](images/export.png) | ![Email](images/email.png) |

| AI Avatar Video |
|-----------------|
| ![Video](images/video.png) |

---

## 🧩 System Architecture

QuickMeet operates through modular pipelines that handle audio/video processing, natural language understanding, and multi-format output generation.

![System Architecture](images/system-architecture.png)

---

## 🛠️ Tech Stack

### Frontend
- HTML5, CSS3, JavaScript (ES6+)
- Bootstrap / Tailwind CSS

### Backend
- Python 3.13.2
- Flask, Flask-CORS

### NLP & AI
- HuggingFace Transformers (BART)
- SentenceTransformers (`all-MiniLM-L6-v2`)
- NLTK, SpaCy
- Regex for action item extraction

### Cloud Services
- **AWS Transcribe** – Audio-to-Text
- **AWS S3** – Cloud storage
- **AWS SES** – Email delivery
- **HeyGen API** – AI avatar video generation

---

## 🔄 How It Works

1. **Upload** audio/video files from a meeting.
2. **Transcribe** audio using AWS Transcribe.
3. **Summarize** with HuggingFace BART model (based on length).
4. **Extract** action items using rule-based regex & NLP.
5. **Search** with semantic similarity (no keyword needed).
6. **Export** insights to PDF or PPT.
7. **Deliver** via email or AI avatar video.

---

## 📁 Project Structure

```bash
QuickMeet/
├── main/                             # Core Flask backend
│   └── app.py
├── templates/                        # HTML templates
├── static/                           # CSS or other frontend static files
├── uploads/                          # Uploaded files (audio/video)
├── images/                           # Screenshots for README
│   ├── upload.png
│   ├── transcript.png
│   ├── summary.png
│   ├── search.png
│   ├── export.png
│   ├── email.png
│   ├── video.png
│   └── system-architecture.png
├── Scripts/                          # Any utility scripts
├── Outputs/                          # Generated summary/PDF/PPT outputs
├── Email_sending/                    # AWS SES integration code
├── Pdf,ppt generation/               # PDFKit and python-pptx related scripts
├── Semantic_search/                  # Vector similarity search
├── Summary_Action items generation/  # NLP + regex logic
├── Transcription/                    # AWS Transcribe handlers
├── Video_generation/                 # HeyGen integration
├── LICENSE
└── README.md
