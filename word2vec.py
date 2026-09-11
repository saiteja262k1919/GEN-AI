from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')

text = input("Enter a sentence: ")

# Convert to lowercase and tokenize
tokens = word_tokenize(text.lower())

# Word2Vec expects a list of tokenized sentences
sentences = [tokens]

# Train the model (CBOW)
model = Word2Vec(
    sentences,
    vector_size=100,
    window=5,
    min_count=1,
    workers=4,
    sg=0        # CBOW
)

print("\nVocabulary:")
print(model.wv.index_to_key)

word = input("\nEnter a word to get its vector: ").lower()

if word in model.wv:
    print("\nWord Vector:")
    print(model.wv[word])
else:
    print("Word not found in vocabulary.")