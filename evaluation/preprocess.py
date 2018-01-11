import re
import nltk
from nltk.tokenize import word_tokenize as w_t,sent_tokenize as s_t
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import SnowballStemmer
from nltk.stem import WordNetLemmatizer 
from nltk.stem.lancaster import LancasterStemmer
from . import PickleIO as pio
import os
java_path = "C:\\Program Files (x86)\\Java\\jdk1.8.0_25\\bin\\java.exe"
os.environ['JAVAHOME'] = java_path
from nltk.tag.stanford import StanfordPOSTagger

def tokenize(txt):
    '''
   For tokenizing a paragraph to sentences to words
    '''
    doc = []
    for sent in s_t(txt):
        sent = sent.replace("n't"," not")
        wrds = re.findall(r'\w+',sent)
        word = " ".join(wrds)#.lower()
        for wrd in w_t(word):
            doc.append(wrd)
    return doc

def remove_stopwords(words,lang='english'):
    '''
    To remove frequently used words in English language
    '''
    rem_words = []
    stop_words = set(stopwords.words(lang))
    for w in words:
        if w not in stop_words:
            rem_words.append(w)
    return rem_words

def stemming(words_stemm, type="PorterStemmer", lang="english", encoding="utf8"):
    '''
    To take words to root level either through end truncation or to dictionary meaning
    Both algorithms are not perfect
    '''
    supported_stemmers = ["PorterStemmer","SnowballStemmer","LancasterStemmer","WordNetLemmatizer"]
    stemm = []
    if type == "PorterStemmer":
        stemmer = PorterStemmer()
        for word in words_stemm:
            stemm.append(stemmer.stem(word))#.encode(encoding))
    if type == "SnowballStemmer":
        stemmer = SnowballStemmer(lang)
        for word in words_stemm:
            stemm.append(stemmer.stem(word))
    if type == "LancasterStemmer":
        stemmer = LancasterStemmer()
        for word in words_stemm:
            stemm.append(stemmer.stem(word))
    if type == "WordNetLemmatizer": #TODO: context
        wnl = WordNetLemmatizer()
        for word in words_stemm:
            stemm.append(wnl.lemmatize(word))
    return stemm

def To_include_not(m):
    lst = []
    for i in range(len(m)):
        toc = m[i][0]
        if m[i][0] == "not":
            if i != len(m)-1:
                if m[i+1][1] in {'RB','RBR','RBS','JJ','JJR','JJS','VB','VBD','VBG','VBN','VBP','VBZ'}:
                    toc = m[i][0] + m[i+1][0]
        if m[i-1][0] == "not":
            continue
        lst.append(toc)
    return lst

def quality(tokenized_words,way ):
    '''
    To get only verbs, adverbs and adjectives
    '''
    new_words = []
    if way == "Stanford":
        jar = os.getcwd() + '\\stanford-postagger-2017-06-09\\stanford-postagger.jar'
        model = os.getcwd() + '\\stanford-postagger-2017-06-09\\models\\english-left3words-distsim.tagger'
        pos_tagger = StanfordPOSTagger(model, jar)# ,encoding='utf8')
        pos_tagger.java_options='-mx1000m'
        tagged_words = pos_tagger.tag(tokenized_words)
    else:
        tagged_words = nltk.pos_tag(tokenized_words)
    for i in tagged_words:
        if i[1] in {'RB','RBR','RBS','JJ','JJR','JJS','VB','VBD','VBG','VBN','VBP','VBZ'}:
            new_words.append(i)
    new_words = [ (x.lower(),y) for x, y in new_words]
    new_words_2 = To_include_not(new_words)
    return new_words_2



'''
txt = ' I teach Science' 
#txt = 'My name is Mr. Rajesh Titung. I\'m here. I will not be to teaching you all about NLP. Do you understanding?. Its about reading. The one who reads becomes educated and sees things. I am friendly friend. I am not negro. Albert Einstein is the greatest scientist alive'            
tokenized_words = tokenize(txt)
remaining_words = remove_stopwords(tokenized_words)
trunc = quality(remaining_words)
trunc2 = remove_stopwords(trunc)
#trunc = quality(tokenized_words)
stem = stemming(trunc2)
print(stem)
'''
#train_posTagger()
#getTagger()
