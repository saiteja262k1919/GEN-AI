import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download resources (Run only once)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

text = input("Enter a sentence: ")

# Standard stopwords
standard_stopwords = set(stopwords.words("english"))

# Contextual stopwords
contextual_stopwords = {
    "today", "currently", "actually",
    "basically", "simply", "really", "just"
}

# Combine stopwords
all_stopwords = standard_stopwords.union(contextual_stopwords)

# Tokenize
words = word_tokenize(text)

# Remove stopwords
filtered_words = [
    word for word in words
    if word.lower() not in all_stopwords
]

print("\nFiltered Tokens:")
print(filtered_words)