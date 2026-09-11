import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

text = input("Enter a sentence: ")

words = word_tokenize(text)

stop_words = set(stopwords.words("english"))

filtered_words = [
    word for word in words
    if word.lower() not in stop_words and not word.isdigit()
]

print("\nFiltered Tokens:")
print(filtered_words)