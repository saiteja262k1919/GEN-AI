import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download resources (Run only once)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

text = input("Enter a sentence: ")

# Convert sentence into words
words = word_tokenize(text)
print("my word token",words)

# Load English stopwords
stop_words = set(stopwords.words('english'))
print("my_stopwords",stop_words)
# Remove stopwords
filtered_words = [word for word in words if word.lower() not in stop_words]
print("my_stopwords",stop_words)
# print("\nOriginal Words:")
# print(words)

# print("\nWords After Stopword Removal:")
# print(filtered_words)
