 💻 🔥 PYTHON CODE (GEN-AI Developer Level)

## Install first

```bash
pip install nltk spacy textblob
python -m spacy download en_core_web_sm
```

---

## Full Pipeline Code

```python
import nltk
import spacy
from textblob import TextBlob
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


nltk.download('punkt')
nltk.download('stopwords')

# Load model
nlp = spacy.load("en_core_web_sm")

text = "Hi, my name is Ravi. I live in Chennai. This product is very bad"

# 🔹 1. Preprocessing
tokens = word_tokenize(text.lower())
stop_words = set(stopwords.words('english'))
clean_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]

print("Clean Tokens:", clean_tokens)

# 🔹 2. Lemmatization
doc = nlp(" ".join(clean_tokens))
lemmas = [token.lemma_ for token in doc]
print("Lemmas:", lemmas)

# 🔹 3. Named Entity Recognition
for ent in doc.ents:
    print("Entity:", ent.text, "| Type:", ent.label_)

# 🔹 4. Sentiment Analysis
sentiment = TextBlob(text).sentiment
print("Sentiment:", sentiment)
```

---

# 🔥 OUTPUT (Example)

```
Clean Tokens: ['hi', 'name', 'ravi', 'live', 'chennai', 'product', 'bad']
Lemmas: ['hi', 'name', 'ravi', 'live', 'chennai', 'product', 'bad']
Entity: Ravi | PERSON
Entity: Chennai | GPE
Sentiment: Negative
```

---