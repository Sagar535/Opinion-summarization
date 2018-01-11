import numpy as np
from . import alphasolvers
from . import SqliteDB as sdb
from . import dotproduct as dp
from . import PickleIO as pio

##cvxopt is for optimization
##if aafaile optimization garney ho vaney
##cvxopt aafai lekhnu parxa

class Support_Vector_Machine:
    def __init__(self, C=None):
        self.C = C
        if self.C is not None: self.C = float(self.C)
    
    #train
    def train(self, X, y, n_samples):#, n_features):
        no_doc = n_samples
        db_name='decisionvector.db'

        loadorsolve=input("a to load: b to solve")

        if loadorsolve=='b':
            Kernel = np.zeros((no_doc, no_doc))
            
            #initialization of kernel matrix
            for i in range(no_doc):
                for j in range(no_doc):
                    Kernel[i,j]= dp.DotProduct(X[i],X[j]) #kun dot product use garne specify gar
            print("kernel matrix made success")
            alphas = alphasolvers.Alpha_Calculator(Kernel, no_doc, y, self.C)
            #print(alphas)

            pio.filedumper('alphas.pkl',alphas)

        elif loadorsolve=='a':
            alphas=pio.filegetter('evaluation/alphas.pkl')
        #Support Vectors
        else:
            print("retarded input")
            return -1
        
        sv = alphas > 1e-5
        tmpXlist, tmpylist=[],[]
        self.alphas = alphas[sv]
        print(len(X),len(y))
        #self.y = y[sv]
        tmp=0
        for values in sv: 
            if values==True:
                tmpXlist.append(X[tmp])
                tmpylist.append(y[tmp])
                tmp+=1
        self.sv = tmpXlist
        self.y = tmpylist
        tmpXlist=[]
        tmpylist=[]
        ##Support Vectors End
        #discriminator

        W=[]
        pointer=0
        
        for vector in self.sv:
            ay=self.alphas[pointer]*self.y[pointer]
            for component in vector:
                comp_val=dp.ScalarProduct(ay, component)
                W.append(comp_val)
            pointer+=1
        #self.W=W
        pointer=0
        sdb.data_entry(db_name, W)
        W=[]
        ##discriminator
        ##let's test

    def predict(self, features):
        db_name='evaluation/decisionvector.db'
        W=[]
        pos=[]
        for X in features:
            for Y in X:
                pos.append(Y[0])
        W = sdb.get_data(db_name, pos)
        clf = np.sign(dp.DotProduct(features[0],W))
        return clf
