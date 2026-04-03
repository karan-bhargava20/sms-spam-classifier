import streamlit as st
import pickle
import string
import nltk
import os
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Add a local nltk_data directory (Render doesn't have nltk preinstalled)
nltk_data_dir = os.path.join(os.path.dirname(__file__), "nltk_data")
os.makedirs(nltk_data_dir, exist_ok=True)
nltk.data.path.append(nltk_data_dir)

# Download necessary NLTK corpora if not present
nltk.download('punkt', download_dir=nltk_data_dir, quiet=True)
nltk.download('stopwords', download_dir=nltk_data_dir, quiet=True)
nltk.download('punkt_tab', download_dir=nltk_data_dir, quiet=True)

ps = PorterStemmer()

def text_transform(text):
    text = text.lower()
    text = nltk.word_tokenize(text)  # default is english
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)

# Load pre-trained vectorizer and model
with open('vectorizer.pkl', 'rb') as f:
    tfidf = pickle.load(f)
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Email / SMS Spam Classifier")

input_sms = st.text_area("Enter your message")

if st.button("Predict"):
    if input_sms.strip() == "":
        st.warning("Please enter a message to predict.")
    else:
        transform_sms = text_transform(input_sms)
        vector_input = tfidf.transform([transform_sms])
        result = model.predict(vector_input)[0]
        if result == 1:
            st.header("Spam")
        else:
            st.header("Not Spam")