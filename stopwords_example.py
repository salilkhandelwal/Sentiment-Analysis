from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_string = "My name is Salil. I am a boy who loves to code."
tokens = word_tokenize(example_string)
stop_words = set(stopwords.words("english"))
filter_words = []
for w in tokens:
    if w not in stop_words:
        filter_words.append(w)
print(filter_words)
print(stop_words)

