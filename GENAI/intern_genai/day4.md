
# DAY 4 NLP MINI PROJECT
# SENTIMENT ANALYZER
# Google Colab Practice Code
# =========================================

# Install required libraries
!pip install nltk textblob -q

# =========================================
# IMPORT LIBRARIES
# =========================================

import nltk
from textblob import TextBlob

# download nltk data
nltk.download('punkt')
nltk.download('punkt_tab')

# =========================================
# USER INPUT
# =========================================

text = input("Enter your sentence: ")

# =========================================
# TEXT PREPROCESSING
# =========================================

# convert lowercase
clean_text = text.lower()

print("\nLowercase Text:")
print(clean_text)

# =========================================
# TOKENIZATION
# =========================================

tokens = nltk.word_tokenize(clean_text)

print("\nTokens:")
print(tokens)

# =========================================
# SENTIMENT ANALYSIS
# =========================================

blob = TextBlob(clean_text)

sentiment_score = blob.sentiment.polarity

print("\nSentiment Score:", sentiment_score)

# =========================================
# PREDICTION
# =========================================

if sentiment_score > 0:
    print("\nPrediction: Positive 😊")

elif sentiment_score < 0:
    print("\nPrediction: Negative 😡")

else:
    print("\nPrediction: Neutral 😐")s