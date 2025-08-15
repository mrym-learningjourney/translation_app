import re

def clean_text(text):
    """Clean and preprocess text"""
    text = str(text).lower()
    text = re.sub(r'[^a-zA-ZÀ-ÿ\s]', '', text)  # Keep French accented characters
    text = re.sub(r'\s+', ' ', text).strip()
    return text

