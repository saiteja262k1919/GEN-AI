import nltk
from nltk.tokenize import sent_tokenize

# Download required resources (run only once)
nltk.download('punkt')
nltk.download('punkt_tab')

text = input("Enter a paragraph: ")

sentences = sent_tokenize(text)

print("\nSentence Tokens:")
for i, sentence in enumerate(sentences, start=1):
    print(f"{i}. {sentence}")