import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from . import PickleIO as pio
import numpy as np

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stems = []
    for item in tokens:
        stems.append(PorterStemmer().stem(item))
    return stems

def VectorListGen(X, n_samples):
    #print(n_samples)
    vector=[]
    Vec_List=[]

    for val in range(n_samples):
        vector=[]
        feature_index = X[val,:].nonzero()[1]
        tfidf_scores = zip(feature_index, [X[val, x] for x in feature_index])
        for (i,s) in tfidf_scores:
            component=[]
            component.append(i)
            component.append(s)
            vector.append(component)
        Vec_List.append(vector)
    return Vec_List

def tfidfsample(text,code):
    vectorizer=pio.filegetter('tfidfdatamv.pkl')

    Y=vectorizer.transform(text)
    #print(Y)

    Test=VectorListGen(Y,1)

    return Test

def Compress(text_list):
    predecessor=text_list[0]
    for current in text_list[1:]:
        if current in predecessor:
            text_list.remove(current)
        predecessor=current
    current=text_list[0]
    for newcommer in text_list[1:]:
        temp=newcommer
        if current in newcommer:
            text_list.remove(newcommer)
        current=temp
    return text_list[:11]

def Visualization(obj_list):
    pos=[]
    neg=[]
    pos_val, neg_val=0,0
    pos_per, neg_per=0,0
    total=len(obj_list)
    top_n = 25
    for items in obj_list:
        if items.sent>0:
            pos.append(items.text)
            pos_val+=1
        else:
            neg.append(items.text)
            neg_val+=1
    pos_per=pos_val/total
    neg_per=neg_val/total
    vectorizer= TfidfVectorizer(stop_words='english',ngram_range=(1,3))#tokenizer=tokenize, stop_words='english')
    ##pos
    X = vectorizer.fit_transform(pos)
    indices = np.argsort(vectorizer.idf_)[::-1]
    features = vectorizer.get_feature_names()
    top_features_pos = [features[i] for i in indices[:top_n]]
    top_features_pos=Compress(top_features_pos)
    ##neg
    Y = vectorizer.fit_transform(neg)
    indices = np.argsort(vectorizer.idf_)[::-1]
    features = vectorizer.get_feature_names()
    top_features_neg = [features[i] for i in indices[:top_n]]
    top_features_neg=Compress(top_features_neg)
    
    return pos_per, neg_per, top_features_pos, top_features_neg

def tfidfvec(documents,code):
    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    X = tfidf.fit_transform(documents)
    #print(tfs[0])
    pio.filedumper('tfidfdata'+code+'.pkl',tfidf)

    n_samples, n_features= X.shape
    
    VectoList=VectorListGen(X, n_samples)

    return VectoList, n_samples, n_features
