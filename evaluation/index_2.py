from . import preprocess
from . import retrieve
from . import general 
from . import tfidf_sklearn
from . import load
from . import PickleIO as pio
from . import SqliteDB as sdb
#from . import SupportVM
from . SupportVM import Support_Vector_Machine
import os

def prep_2(file):
    read = retrieve.data_retrieval(file)
    return read

def preprocess_index(read):
    doc = []
    rem_words = []
    intermed = []
    final = []
    final2 = []
    for each_par in read:
        doc.append(preprocess.tokenize(each_par))
    #Stopword Removal
    for par in doc:
        rem_words.append(preprocess.remove_stopwords(par))
    #To include only verbs, adverbs and adjectives
    #preprocess.post_tagger()
    #pos_tagger=pio.filegetter('postagger.pkl')
    for parg in rem_words:
        final.append(preprocess.quality(parg,"nltk_tagger"))
    #final=preprocess.quality(rem_words)
    #Intermediate process
    for parleg in final:
        final2.append(preprocess.remove_stopwords(parleg))
    #Stemming|Lemmatizing
    for ava in final2:
        intermed.append(preprocess.stemming(ava))
    return intermed

def tfidftrainer():
    lst,y,code = load.category_selector()
    corpora_preprocessed = preprocess_index(lst)
    corpora4tfidf = general.token2sent(corpora_preprocessed)
    tfidf_of_corpora, no_samples, no_words = tfidf_sklearn.tfidfvec(corpora4tfidf)
    #to save to file
    file = 'matrix_' + code + '.pkl'
    yfile="y_value.pkl"
    pio.filedumper(file,tfidf_of_corpora)
    pio.filedumper(yfile,y)

    return no_samples, no_words

def loadme():
    itemlist=[]
    val_y=[]
    itemlist=pio.filegetter("matrix_mv.pkl")
    val_y=pio.filegetter("y_value.pkl")
    
    print("complete")
    return itemlist, val_y
    
def splitter(Data, a, b):
    len1=int(len(Data)*(a/(a+b)))
    list1=Data[:len1]
    list2=Data[len1:]
    return list1, list2


def testdata(test):
    test_text=[]
    #test_text=['There was a time when I was very jolly and juvenile']
    test_text.append(test)
    ##preprocess
    sample_preprocessed=preprocess_index(test_text)
    sent = general.token2sent(sample_preprocessed)
    tfidf_of_sample=tfidf_sklearn.tfidfsample(sent)
    #print(tfidf_of_sample)
    ##preprocess
    return tfidf_of_sample
    
def testdata2(test_text1):
    test_text=[]
    test_text.append(test_text1)
    tfidf_of_sample=tfidf_sklearn.tfidfsample(test_text)
    #print(tfidf_of_sample)
    ##preprocess
    return tfidf_of_sample
    
def main(test, value = 6):
    db_name='decisionvector.db'
    intlist=[]
    ylist=[]
    Datalist1, Datalist2=[],[]
    y_value1, y_value2=[],[]
    no_samples, no_words=0,0
    SVMachine = Support_Vector_Machine()
    # print(" 1 for train\n",
    #       "2 for load\n",
    #       "3 to split\n",
    #       "4 to train SVM\n",
    #       "5 to create Database\n",
    #       "6 to test data\n",
    #       "7 to test Accuracy\n",
    #       "8 to exit\n")
    userinput = value
    if userinput==1:
        no_samples, no_words=tfidftrainer()
        print("COMPLETE")
    elif userinput==2:
        intlist, ylist=loadme()
        print("SUCCESS")
    elif userinput==3:
        Datalist1, Datalist2 = splitter(intlist,9,1)
        y_value1,y_value2 = splitter(ylist,9,1)
        print("success")
    elif userinput==4:
        SVMachine.train(Datalist1, y_value1, len(y_value1))
        print("success")
    elif userinput==5:
        sdb.create_table(db_name)
    elif userinput==6:
        sample=testdata(test)
        to_ret = SVMachine.predict(sample)
        return to_ret
    elif userinput==7:
        l = []
        count = 0
        for i in range(len(Datalist2)):
            ls = [Datalist2[i]]
            c = SVMachine.predict(ls)
            l.append(c)
        for i in range(len(Datalist2)):
            if y_value2[i] == l[i]:
                count += 1
        accuracy = (count/len(Datalist2))*100
        print('Accuracy:',accuracy)

def mainop(search_keyword):
    SVMachine = Support_Vector_Machine()
    fname = 'final_'+ search_keyword + '.txt'
    path = os.getcwd() + '/Scrapped/Texts'
    file_name = os.path.join(path,fname)
    read = prep_2(file_name)
    doc = general.cat4input(read)
    intermed = preprocess_index(read)#
    doc1 = general.token2sent(intermed)#
    doc2 = general.cat4input(doc1)
    #print(doc2)
    sample=testdata2(doc2)#
    print(SVMachine.predict(sample))

#mainop('adolf+hitler')
#main()
