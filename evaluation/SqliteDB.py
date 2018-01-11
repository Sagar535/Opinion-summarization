import sqlite3
import sys

def create_table(dbname):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS PARAGRAPHS (SN INT PRIMARY KEY NOT NULL, POS TEXT NOT NULL, TFID REAL NOT NULL)')
    print("Database creation successful")
    conn.commit()
    conn.close()

def data_entry(dbname, W):
    num=0
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    for data in W:
        temp=data
        num+=1
        cur.execute("insert or ignore into PARAGRAPHS (SN, POS, TFID) values (?, ?, ?)",(num,str(temp[0]),temp[1]))
    conn.commit()
    conn.close()
    print("Database writing complete")

#X has to be a list of positions
def get_data(dbname, X):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    biglist=[]
    #print("X is printed")
    for dat in X:
        sdat=str(dat)
        cur.execute("SELECT TFID FROM PARAGRAPHS WHERE POS= (?)",(sdat,))
        for row in cur.fetchall():
            multi=[]
            multi.append(dat)
            multi.append(float(".".join(map(str,row))))
            biglist.append(multi)
    conn.close()
    return biglist



               
