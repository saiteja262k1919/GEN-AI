import nltk
from nltk.tokenize import word_tokenize

# Download resources (Run only once)
nltk.download('punkt')
nltk.download('punkt_tab')

# Input sentence
text = input("Enter a sentence: ")

# Tokenize
words = word_tokenize(text.lower())

# Create vocabulary
vocab = sorted(set(words))

print("Vocabulary:")
print(vocab)

print("\nOne-Hot Encoding:\n")

# Generate one-hot vectors
for word in words:
    vector = [1 if word == v else 0 for v in vocab]
    print(f"{word} -> {vector}")