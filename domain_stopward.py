import nltk
from nltk.tokenize import word_tokenize

# Download resources (run only once)
nltk.download('punkt')
nltk.download('punkt_tab')

text = input("Enter a sentence: ")

# Define domain-specific stopwords
domain_stopwords = {
    "nlp", "python", "data", "model",
    "algorithm", "learning", "machine"
}

# Tokenize the text
words = word_tokenize(text)

# Remove domain stopwords
filtered_words = [word for word in words
                  if word.lower() not in domain_stopwords]

print("\nOriginal Tokens:")
print(words)

print("\nAfter Domain Stopword Removal:")
print(filtered_words)