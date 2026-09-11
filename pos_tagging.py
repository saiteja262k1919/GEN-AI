import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

text = input("Enter a sentence: ")

tokens = word_tokenize(text)

tagged = nltk.pos_tag(tokens)

tags = [tag for word, tag in tagged]

count = Counter(tags)

print("\nPOS Tag Counts:")
print(count)