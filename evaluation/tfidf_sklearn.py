import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from . import PickleIO as pio

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

def tfidfsample(text):
    vectorizer=pio.filegetter('tfidfdata.pkl')

    Y=vectorizer.transform(text)
    #print(Y)

    Test=VectorListGen(Y,1)

    return Test
    

def tfidfvec(documents):
    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    X = tfidf.fit_transform(documents)
    #print(tfs[0])
    pio.filedumper('tfidfdata.pkl',tfidf)

    n_samples, n_features= X.shape
    
    VectoList=VectorListGen(X, n_samples)

    return VectoList, n_samples, n_features

    
    '''
    feature_names = tfidf.get_feature_names()
    for col in X.nonzero()[1]:
        print(feature_names[col] , ' - ' , X[0, col])
    '''
    
'''
def tfidfvec(documents):
    stopset=set(stopwords.words('english'))
    tfidf = TfidfVectorizer(stop_words=stopset,use_idf=True, ngram_range=(1,2))
    tfs = tfidf.fit_transform(documents)
    #print(tfs)
    feature_names = tfidf.get_feature_names()
    for col in tfs.nonzero()[1]:
        print(feature_names[col] , ' - ' , tfs[0, col])
'''
