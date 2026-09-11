# from transformers import AutoTokenizer

# # Load a pretrained BERT tokenizer
# tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# text = input("Enter a sentence: ")

# # Perform subword tokenization
# tokens = tokenizer.tokenize(text)

# print("Subword Tokens:")
# print(tokens)
import nltk
from nltk.tokenize import RegexpTokenizer

text = input("Enter a sentence: ")

tokenizer = RegexpTokenizer(r'\w+')

tokens = tokenizer.tokenize(text)

print("Tokens:")
print(tokens)