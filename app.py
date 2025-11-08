from flask import Flask, render_template, request, jsonify
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

app = Flask(__name__)

# LangChain model setup
template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(
    model="llama3.1",
    options={
        "temperature": 0.6,  # lower = faster and more focused
        "num_predict": 256,  # limit max tokens in each response
        "top_k": 40,         # controls randomness
        "top_p": 0.9
    }
)

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Conversation memory
context = ""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global context
    data = request.get_json()
    user_input = data.get("message", "")
    print("User:", user_input)

    result = chain.invoke({"context": context, "question": user_input})
    print("Bot:", result)

    response = str(result)
    context += f"\nUser: {user_input}\nAI: {response}"
    return jsonify({"reply": response})


if __name__ == "__main__":
    app.run(debug=True)
