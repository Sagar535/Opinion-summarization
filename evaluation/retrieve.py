from . import preprocess
import re
from . import general

def retrive_frm_db(file):
    '''
       Retrieves scrapped data from database
    '''
    read = open(file,'r',encoding='utf-8').readlines()
    return read

def data_retrieval(file):
    '''
     Removes unwanted empty lines and prepares corpora
    '''
    read = retrive_frm_db(file)
    doc = []
    for i in read:
        if i !="\n":
            doc.append(i)
    return doc

def retrieve_out_data(file):
    '''
    Retrieve either training or test data
    '''
    read = open(file,'r').readlines()
    clean = general.cleanhtml(str(read))
    count = 0
    for i in clean:
        print(i)
        count = count + 1
        if count > 20:
            break


'''
#file = "C:\\Users\\Rajesh\\Desktop\\Requests\\Info\\final_albert+einstein.txt"
file = "C:\\Users\\Rajesh\\Desktop\\Requests\\jpt.txt"
read = data_retrieval(file)
#read = retrive_frm_db(file)
print(read)
'''
#file = "C:\\Users\\Rajesh\\Desktop\\Requests\\pros_cons\\IntegratedCons.txt"
#retrieve_out_data(file)
