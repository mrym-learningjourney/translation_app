from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import nltk
from nltk.tokenize import word_tokenize
import pickle
import numpy as np
import re

def clean_text(text):
    """Clean and preprocess text"""
    text = str(text).lower()
    text = re.sub(r'[^a-zA-ZÀ-ÿ\s]', '', text)  # Keep French accented characters
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Load your trained model
model = load_model("model/translation_model_bilstm.h5")

# Load English tokenizer
with open("model/english_tokenizer.pkl", "rb") as f:
    eng_tokenizer = pickle.load(f)

# Load French tokenizer
with open("model/french_tokenizer.pkl", "rb") as f:
    fr_tokenizer = pickle.load(f)

def predict_translation(input_sentence):

    input_sentence = clean_text(input_sentence)
    input_sentence = word_tokenize(input_sentence)
    input_sequence = eng_tokenizer.texts_to_sequences([input_sentence])

    input_padded = pad_sequences(input_sequence, maxlen=15, padding='post')

    predicted_sequence = model.predict(input_padded)

    predicted_words = []
    for i in range(predicted_sequence.shape[1]):
        predicted_word_index = np.argmax(predicted_sequence[0, i, :])
        if predicted_word_index != 0:
            predicted_word = fr_tokenizer.index_word.get(predicted_word_index)
            predicted_words.append(predicted_word)

    predicted_sentence = ' '.join(predicted_words)

    return predicted_sentence