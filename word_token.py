# import nltk
# from nltk.tokenize import word_tokenize

# # Run only once
# nltk.download('punkt')

# text = input("Enter a sentence: ")

# words = word_tokenize(text)

# print("Word Tokens:")
# print(words)
import nltk
from nltk.tokenize import word_tokenize

# Download resources (only the first time)
nltk.download('punkt')
nltk.download('punkt_tab')

text = input("Enter a sentence: ")

words = word_tokenize(text)

print("Word Tokens:")
print(words)