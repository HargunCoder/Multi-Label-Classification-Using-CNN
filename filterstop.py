from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#import nltk
#nltk.download('stopwords')

#import nltk
#nltk.download('punkt')

#exampl_sentence="you boy"
stop_words= set(stopwords.words("english"))

#print(stop_words)
def rem_stop(exampl_sentence):
    words= word_tokenize(exampl_sentence)
    filtered_sentence = []
    for w in words:
        if w not in stop_words:
            filtered_sentence.append(w)
    return filtered_sentence

#print (filtered_sentence)

#def con():
#    print ("connected")