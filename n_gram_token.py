import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

nltk.download('punkt')
nltk.download('punkt_tab')

text = input("Enter a sentence: ")
n = int(input("Enter the value of N: "))

tokens = word_tokenize(text)

result = list(ngrams(tokens, n))

print(f"\n{n}-Grams:")
for gram in result:
    print(gram)