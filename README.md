# 🤖 J.A.R.V.I.S – Personal AI Assistant

**J.A.R.V.I.S (Just A Rather Very Intelligent System)** is your personal command-line AI assistant built using Python and the Groq API. It responds intelligently to your queries, remembers context, and can provide real-time responses using a custom knowledge prompt setup.

---

## 🚀 Features

- 🔐 Owner authentication system
- 🌐 Real-time awareness (date, time)
- 💬 Conversational context memory (`ChatLog.json`)
- 🌍 Multilingual input handling (auto-detects Hindi/Bengali and responds in English)
- 🧠 Smart system prompts for role definition
- 📁 Organized environment and configuration using `.env` file
- ✨ Streamed response generation using Groq API (LLaMA 3)
- 📦 Requirements managed through a `Requirements.txt` file

---

## 📁 Project Structure

J.A.R.V.I.S/
│
├── Backend/
│ ├── Chatbot.py # Main assistant logic
│ └── Data/
│ └── ChatLog.json # Chat history log
│
├── .env # Environment variables
├── Requirements.txt # Required Python packages
└── README.md # This file


---

## ⚙️ Requirements

Install all dependencies in one command:

```bash
pip install -r Requirements.txt
