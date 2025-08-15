from flask import Flask, render_template, request
from model.translator import predict_translation

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    english_text = request.form["english_text"]

    french_text = predict_translation(english_text)

    return render_template("index.html", english_text=english_text, translated_text = french_text)