# Chatbot
Ollama-python chatbot 🤖 --> I have used llama3.1 ollama model in this Chatbot project. 

---

## 💬 AI Chatbot using LangChain + Ollama + Flask

A simple yet powerful **AI Chatbot web application** built with **LangChain**, **Ollama**, and **Flask**, designed for local LLMs like **Llama 3.1** and **DeepSeek-R1**.
It provides a clean, responsive web interface for chatting with your locally-hosted models — directly from your browser!

---

### 🚀 Features

* 🧠 Uses **LangChain + Ollama** for natural conversation
* 🌐 Web-based chat interface (HTML, CSS, JS, Flask backend)
* ⚡ Fast response rendering
* 💾 Context-aware conversations (memory included)
* 🎨 Stylish floating chat UI at bottom-right corner
* 🧩 Works with **any Ollama model** (Llama, DeepSeek, Mistral, etc.)

---

### 🛠️ Tech Stack

| Layer         | Technologies Used                       |
| ------------- | --------------------------------------- |
| **Frontend**  | HTML, CSS, JavaScript                   |
| **Backend**   | Python (Flask)                          |
| **AI Engine** | LangChain + OllamaLLM                   |
| **Models**    | Llama 3.1 8B / DeepSeek-R1 8B / Llama 2 |

---

### ⚙️ Installation

#### 1️⃣ Clone this repository

```bash
git clone https://github.com/<your-username>/chatbot-ollama.git
cd chatbot-ollama
```

#### 2️⃣ Create a virtual environment

```bash
python -m venv chat
chat\Scripts\activate        # (Windows)
# or
source chat/bin/activate     # (Mac/Linux)
```

#### 3️⃣ Install dependencies

```bash
pip install flask langchain_ollama langchain_core
```

#### 4️⃣ Install and run Ollama

Download Ollama from 👉 [https://ollama.ai/download](https://ollama.ai/download)

Then pull your preferred model:

```bash
ollama pull llama3.1
# or
ollama pull deepseek-r1:8b
```

Start Ollama server (it usually runs automatically):

```bash
ollama serve
```

### 📸 Screenshots

| Web Chat UI                                   | Example Conversation                    |
| --------------------------------------------- | --------------------------------------- |
| ![Chat UI Screenshot](assets/screenshot1.png) | ![Chat Example](assets/screenshot2.png) |

---

### 💡 Future Improvements

* Add multi-model selector
* Chat memory persistence
* UI animations & dark mode
* API support for integration

---

### 🤝 Contributing

Pull requests are welcome!
If you’d like to improve UI or speed, feel free to fork the repo and submit your ideas.

---

### 🧾 License

This project is licensed under the **MIT License** — feel free to use and modify it.


