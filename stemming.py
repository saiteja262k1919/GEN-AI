import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download resources (Run only once)
nltk.download('punkt')
nltk.download('punkt_tab')

text = input("Enter a sentence: ")

# Tokenize
words = word_tokenize(text)

# Create Porter Stemmer object
ps = PorterStemmer()

# Perform stemming
stemmed_words = [ps.stem(word) for word in words]

print("\nOriginal Words:")
print(words)

print("\nStemmed Words:")
print(stemmed_words)