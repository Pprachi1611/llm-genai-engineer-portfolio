# 🤖 AI Study Helper (CLI)

A simple command-line AI tool that helps you **understand concepts, summarize text, and generate notes** using a Large Language Model (LLM).

---

## 🧠 What is an LLM?

A **Large Language Model (LLM)** is an AI system trained on massive text data that can understand and generate human-like responses.

This project uses an LLM via API to process user input and return useful, simplified outputs.

---

## 🚀 Features

* 📖 Explain concepts in simple terms
* ✂️ Summarize long text
* 📝 Generate clean bullet-point notes
* 🔁 Continuous chat loop (CLI-based interaction)
* 🔐 Secure API key handling using `.env`

---

## 🛠️ Tech Stack

* Python
* `requests` (API calls)
* `python-dotenv` (environment variables)
* LLM API (via OpenRouter)

---

## 📦 Project Structure

```
day-3-ai-study-helper/
│
├── app.py
├── .env           # API key (not pushed)
├── .gitignore
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/day-3-ai-study-helper.git
cd day-3-ai-study-helper
```

---

### 2. Install dependencies

```
pip install requests python-dotenv
```

---

### 3. Add your API key

Create a `.env` file:

```
OPENROUTER_API_KEY=your_api_key_here
```

---

### 4. Run the app

```
python app.py
```

---

## 💻 Usage

```
Choose Mode:
1 → Explain
2 → Summarize
3 → Generate Notes
```

Type your query and get an AI-generated response instantly.

Type `exit` anytime to quit.

---

## 🧠 What I Learned

* How to integrate an LLM API into a Python app
* Basics of prompt engineering
* Handling user input in a CLI loop
* Managing API keys securely using environment variables

---

## ⚠️ Notes

* The app depends on API availability and free-tier limits
* Responses may vary depending on the model used

---

## 📌 Future Improvements

* Add conversation memory
* Build a web UI (Streamlit)
* Add file upload for summarization
* Convert into a full AI assistant

---

## 📜 License

This project is for learning purposes.
