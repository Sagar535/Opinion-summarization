import pickle

def filedumper(filename, data):
    with open(filename,'wb') as fp:
        pickle.dump(data, fp)

def filegetter(filename):
    with open(filename,'rb') as fp:
        temp = pickle.load(fp)
    return temp
