# BrainSnap — Turn lecture materials into micro-learning brain "nourishment" reels

**BrainSnap** converts dense study material (slides, PDFs, lecture notes, textbook chapters) into
short, vertical, meme-style reels with AI voice and auto-captions — same format people already
consume for hours, but with study concepts instead of brain-rot.

---

## ✨ What BrainSnap does

1) **Upload** slides / textbook chapter (PDF, PPT, images)  
2) **AI rewrites and organizes** the content into 10–30s micro-lessons
3) **AI voiceover** narrates each micro-script  
4) **Meme background + captions** are auto-composited  
5) **Export** a list of reels to download or view on the webapp

---

## 🧱 MVP Architecture (planned)

| Layer | Choice |
|------|--------|
| Backend API | Flask (Python) |
| Background processing | Celery or RQ |
| Storage | S3 (or local for dev) |
| LLM (summaries/scripts) | Gemini API |
| TTS | TBD |
| Video assembly | TBD |
| Frontend | Basic React or simple HTML form for v0 |

---

## 🎯 MVP Scope — v0.1

- File upload (PDF/PPT/images)
- Extract text (OCR fallback if needed)
- Generate 8–25 micro-scripts per input
- Generate TTS audio per script
- Compose vertical video with **fixed meme background pack**
- Auto-captions from TTS transcript
- Download or view reels

### Current Version TODO

Backend
- [ ] Create project structure
- [ ] Implement functionality to extract text from PDFs
- [ ] Integrate Gemini API to generate scripts
- [ ] Set up other AI APIs for voice-over
- [ ] Implement reel creation pipeline
- [ ] Set up basic REST endpoints
Storage
- [ ] Set up DB
- [ ] Set up S3
Frontend
- [ ] Create frontend to upload files
- [ ] Create frontend to view/download reels

---

## 🛣 Roadmap

**v0.2**
- “Exam-mode” (filter only exam-relevant concepts or let user choose which concepts they want to make reels for)
- Deep vs surface mode (and the amount of reels they want to make)

**v0.3**
- Add quiz feature
- Add chatbot feature for live Q&A on lecture materials
- Spaced repetition from viewed reels

**v0.4**
- Improve reel generation quality by generating more reels for topics that the user have trouble on for the quiz
- User accounts & project history
- Credit / quota system for generation
- Classroom or team sharing mode

---

## 🚧 Local Development (draft)

```bash
# clone
git clone https://github.com/<your-username>/brainsnap.git
cd brainsnap

# create venv or conda env

# install core backend deps
pip install -r requirements.txt

# run flask (dev)
flask --app brainsnap.api run --reload
