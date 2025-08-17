from flask import Flask, render_template, request
from model.translator import predict_translation
import nltk

for resource in ["punkt", "punkt_tab"]:
    try:
        nltk.data.find(f"tokenizers/{resource}")
    except LookupError:
        nltk.download(resource)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    english_text = request.form["english_text"]

    french_text = predict_translation(english_text)

    return render_template("index.html", english_text=english_text, translated_text = french_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)