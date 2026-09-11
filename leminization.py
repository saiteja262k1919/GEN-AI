import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download resources (Run only once)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')

text = input("Enter a sentence: ")

# Tokenize
words = word_tokenize(text)

# Create lemmatizer object
lemmatizer = WordNetLemmatizer()

# Lemmatize each word
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

print("\nOriginal Words:")
print(words)

print("\nLemmatized Words:")
print(lemmatized_words)