from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import random
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import numpy as np

# Add the specific path to the nltk data
nltk.data.path.append('C:\\Users\\divya\\AppData\\Roaming\\nltk_data\\corpora\\nltk__data')
lemmatizer = WordNetLemmatizer()

# Load dataset
with open('data.json') as file:
    data = json.load(file)

def preprocess_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens if token.isalnum()]
    return ' '.join(tokens)

patterns = []
tags = []
responses = {}
for intent in data['intents']:
    for pattern in intent['patterns']:
        patterns.append(preprocess_text(pattern))
        tags.append(intent['tag'])
    responses[intent['tag']] = intent['responses']

vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_df=0.75, min_df=1)
X = vectorizer.fit_transform(patterns)
y = np.array(tags)
model = LogisticRegression(solver='liblinear', multi_class='ovr')
model.fit(X, y)

default_response = "Sorry, I can only provide you with the information available on the website. If the information you ask is beneficial for the students then surely we will try to add it."

app = Flask(__name__)
CORS(app)  # Enable CORS for your Flask app
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('message')
    user_input = preprocess_text(user_input)
    vectorized_text = vectorizer.transform([user_input])
    prediction = model.predict(vectorized_text)[0]
    probas = model.predict_proba(vectorized_text)[0]
    
    print(f"User Input: {user_input}, Prediction: {prediction}, Probabilities: {probas}")
    
    confidence_threshold = 0.25  # Lowered threshold for better match
    if max(probas) < confidence_threshold:
        return jsonify({"response": default_response})
    
    response = random.choice(responses[prediction])
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(port=5000)
