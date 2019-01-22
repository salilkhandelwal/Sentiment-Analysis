import nltk
from nltk.corpus import state_union
from nltk.tokenize import word_tokenize
from nltk.tokenize import PunktSentenceTokenizer

train_txt = state_union.raw("2005-GWBush.txt")
test_txt = state_union.raw("2006-GWBush.txt")

train = PunktSentenceTokenizer(train_txt)
test = train.tokenize(test_txt)

def post():
    try:
        for i in test:
            words = word_tokenize(i)
            tag = nltk.pos_tag(words)
            print(tag)

    except Exception as e:
        print(str(e))
        
post()     
        
