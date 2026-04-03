#!/bin/bash

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Download NLTK data
python -m nltk.downloader punkt
python -m nltk.downloader stopwords
python -m nltk.downloader punkt_tab