from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

app = Flask(__name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    question = request.json.get("question")

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": question}
        ]
    )

    return jsonify({"answer": response.choices[0].message.content})


if __name__ == "__main__":
    app.run(debug=True)
