#!/bin/bash

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Download NLTK data to a local directory within the project
mkdir -p nltk_data
python -m nltk.downloader -d nltk_data punkt stopwords