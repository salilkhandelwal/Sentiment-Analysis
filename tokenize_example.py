import nltk

example = "Hello world. How are you? My name is God."
tokens = nltk.word_tokenize(example)
sent_tokens = nltk.sent_tokenize(example)
print sent_tokens
