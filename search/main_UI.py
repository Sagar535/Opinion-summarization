from . import preprocess
from . import retrieve
from . import general
from . import tfidf_sklearn
from . import load
from . import PickleIO as pio
from . import SqliteDB as sdb
from . SupportVM import Support_Vector_Machine
import os
#import mukhya as mkh

class comment(object):
    def __init__(self, text):
        self.text=text
    def Set_Tfidf(self, tfidf):
        self.tfidf=tfidf
    def Sentiment(self, sent):
        self.sent=sent
    def Get_tfidf(self):
        return self.tfidf
        
    

def prep_2(file):
    read = retrieve.data_retrieval(file)
    return read

def preprocess_index(read):
    doc = []
    rem_words = []
    intermed = []
    final = []
    final2 = []
    #if num
    for each_par in read:
        doc.append(preprocess.tokenize(each_par))
    #Stopword Removal
    for par in doc:
        rem_words.append(preprocess.remove_stopwords(par))
    
    #To include only verbs, adverbs and adjectives
    for parg in rem_words:
        final.append(preprocess.quality(parg,"nltk"))#,way="Stanford"))
    
    #Intermediate process
    for parleg in final:
        final2.append(preprocess.remove_stopwords(parleg))
    
    #Stemming|Lemmatizing
    for ava in final2:
        intermed.append(preprocess.stemming(ava))
    
    return intermed

def tfidftrainer():
    #now from internal corpora
    lst,y,code = load.category_selector()
    corpora_preprocessed = preprocess_index(lst)
    corpora4tfidf = general.token2sent(corpora_preprocessed)
    tfidf_of_corpora, no_samples, no_words = tfidf_sklearn.tfidfvec(corpora4tfidf,code)
    #to save to file
    file = 'matrix_' + code + '.pkl'
    yfile="y_value"+code+".pkl"
    pio.filedumper(file,tfidf_of_corpora)
    pio.filedumper(yfile,y)

    return code
    #return no_samples, no_words
    #save.write(tfidf_of_corpora)
    #save.close()
    #input ko tfidf
    #input2svm = tfidf_sklearn.tfidfvec(document4tfidf)

def loadme(code):
    itemlist=[]
    val_y=[]
    itemlist=pio.filegetter("matrix_"+code+".pkl")
    val_y=pio.filegetter("y_value"+code+".pkl")
    
    print("complete")
    return itemlist, val_y
    
def splitter(Data, a, b):
    len1=int(len(Data)*(a/(a+b)))
    list1=Data[:len1]
    list2=Data[len1:]
    return list1, list2


def testdata(code):
    test_text=[]
    #test_text=['There was a time when I was very jolly and juvenile']
    test_text.append(input("Test Text:"))
    ##preprocess
    #sample_preprocessed=preprocess_index(test_text)
    tfidf_of_sample=tfidf_sklearn.tfidfsample(test_text,code)
    #rint(tfidf_of_sample)
    ##preprocess
    return tfidf_of_sample
    
def testdata2(test_text1,code):
    test_text=[]
    test_text.append(test_text1)
    tfidf_of_sample=tfidf_sklearn.tfidfsample(test_text,code)

    return tfidf_of_sample
        
def mainop(search_keyword,code):
    comment_list=[]
    fname = 'final_'+ search_keyword + '.txt'
    path = os.getcwd() + '/search/Scrapped/Texts'
    file_name = os.path.join(path,fname)
    read = prep_2(file_name)
    for i in read:
        obj=comment(str(i))
        text=str(i)
        intermed = preprocess_index([text])
        doc1 = general.token2sent(intermed)
        doc2 = general.cat4input(doc1)
        sample=testdata2(doc2,code)
        
        obj.Set_Tfidf(sample)
        comment_list.append(obj)

    return comment_list

def SVM_Evaluation(TP,FP,TN,FN):
    
    TP1,FP1,FN1,TN1=TP,FP,FN,TN
    print('Confusion Matrix')
    print('\nPridicted')
    print('pos\tneg')
    print(str(TP1)+'\t'+str(FP1)+'\t'+'| pos')
    print(str(FN1)+'\t'+str(TN1)+'\t'+'| neg'+'\t'+'Actual')
    print('\n')        
    accuracy = ((TP+TN)/(TP+FP+TN+FN))*100
    precision= TP/(TP+FP)
    recall=TP/(TP+FN)
    specifity=TN/(TN+FP)
    print('Accuracy :',accuracy)
    print('Precision:',precision)
    print('Recall   :',recall)
    print('Specifity:',specifity)    
    
def main(keyword, value = 8):
    #db_name='decisionvector.db'
    intlist=[]
    ylist=[]
    Datalist1, Datalist2=[],[]
    y_value1, y_value2=[],[]
    no_samples, no_words=0,0
    search_object_list=[]
    CODE=''
    SVMachine = Support_Vector_Machine(150)
    print(" 1 for train\n",
          "2 for load\n",
          "3 to split\n",
          "4 to train SVM\n",
          "5 to create Database\n",
          "6 to test data\n",
          "7 to test Accuracy\n",
          "8 to Person Testing\n",
          "9 for Set Database\n")
    while True:
        userinput = value
        if userinput==1:
            CODE=tfidftrainer()
            db_name='decisionvector'+CODE+'.db'
            print("COMPLETE")
        elif userinput==2:
            intlist, ylist=loadme(CODE)
            print("SUCCESS")
        elif userinput==3:
            Datalist1, Datalist2 = splitter(intlist,4,6)
            y_value1,y_value2 = splitter(ylist,4,6)
            print("success")
        elif userinput==4:
            SVMachine.train(Datalist1, y_value1, len(y_value1),db_name)
            print("success")
        elif userinput==5:
            sdb.create_table(db_name)
        elif userinput==6:
            sample=testdata(CODE)
            print(SVMachine.predict(sample,db_name))
        elif userinput==7:
            TP,FP,FN,TN=0,0,0,0
            count=0
            l = []
            for ls in Datalist2:
                c = SVMachine.predict([ls],db_name)
                l.append(c)
            print(len(y_value2))
            for i in range(len(y_value2)):
                if y_value2[i] == 1 and l[i]==1:
                    TP+=1
                elif y_value2[i] == -1 and l[i]==-1:
                    TN+=1
                elif y_value2[i] == 1 and l[i]==-1:
                    FN+=1
                elif y_value2[i] == -1 and l[i]==1:
                    FP+=1
                else:
                    count+=1
            print(count)
            SVM_Evaluation(TP,FP,TN,FN)
        elif userinput==8:
            # CODE=input("mv for movie, pv for product, tt for twitter: ")
            db_name='search/decisionvectormv.db'
            search=keyword
            search_object_list=mainop(search,'mv')
            print('success')
            for items in search_object_list:
                items.Sentiment(SVMachine.predict(items.Get_tfidf(),db_name))
            pos_per, neg_per, pos_words, neg_words=tfidf_sklearn.Visualization(search_object_list)
            
            print(pos_per)
            print(neg_per)
            print(pos_words)
            print(neg_words)
            return pos_per,neg_per,pos_words,neg_words
        # elif userinput==9:
            
            #mkh.operation()
        else:
            break
    print("!!!WAY OFF!!!")

# main()
