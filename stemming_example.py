from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
##words = ["eaten","eating","eatonic","eately","eaton"]
##for i in words:
    ##print(ps.stem(i))

example_sentence = "All the pythoners doing pythoning have at least once pythoned poorly. Though while pythoning they pyhtonly handled all the problems."    
words = word_tokenize(example_sentence)
for i in words:
    print(ps.stem(i))
