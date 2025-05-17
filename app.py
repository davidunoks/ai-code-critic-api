from flask import Flask, request, jsonify
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import os
import subprocess

model_folder = "ai_code_critic_5000"

# Step 1: Download model if missing
if not os.path.exists(model_folder):
    subprocess.run(["python", "download_model.py"], check=True)

# Step 2: Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_folder)
model = AutoModelForSeq2SeqLM.from_pretrained(model_folder)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Step 3: Flask app
app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    code = data.get("code", "")
    if not code:
        return jsonify({"error": "No code provided"}), 400

    inputs = tokenizer("summarize: " + code, return_tensors="pt", padding=True, truncation=True).to(device)
    outputs = model.generate(
        **inputs,
        max_length=64,
        num_beams=6,
        top_k=50,
        top_p=0.95,
        temperature=0.8,
        do_sample=True,
        early_stopping=True,
        repetition_penalty=1.1
    )
    feedback = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({"feedback": feedback})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
