import csv
import os

def ret(path1):
    lst = []
    y = []
    with open(path1) as csvfile:
        read = csv.reader(csvfile)
        for row in read:
            lst.append(row[0])
            y.append(int(row[1]))
    return lst,y
        
def load(code):
    '''
    Harek bata both pos ra neg ko list ra tesko value pathau6 so 4 lists
    '''
    if code == 'mv':
        file1 = "\\evaluation\\Final_Corpora\\Movie\\neg1.csv"
        path1 = os.getcwd() + file1
        file2 = "\\evaluation\\Final_Corpora\\Movie\\pos1.csv"
        path2 = os.getcwd() + file2
    if code == 'pv':
        file1 = "\\evaluation\\Final_Corpora\\Product_Review\\cons1.csv"
        path1 = os.getcwd() + file1
        file2 = "\\evaluation\\Final_Corpora\\Product_Review\\pros1.csv"
        path2 = os.getcwd() + file2
    lst1,y1 = ret(path1)
    lst2,y2 = ret(path2)
    return lst1,y1,lst2,y2
        
    

def category_selector():
    low_bound_1=0
    low_bound_2=0
    result_type ='' #Either movie review or product review Paxi yeslai check box ma halna par6
    print("Enter 'mv' for Movie Review and 'pv' for product review")
    result_type = input('Enter code:')
    lst1,y1,lst2,y2 = load(result_type)
    single_list=[]
    single_list_y=[]
    ##data merger
    print(len(lst1),len(y1))
    print(len(lst2),len(y2))
    percentile=0.1
    while percentile <= 1:
        high_bound_1=int(percentile*len(lst1))
        high_bound_2=int(percentile*len(lst2))
        single_list.extend(lst1[low_bound_1:high_bound_1])
        single_list.extend(lst2[low_bound_2:high_bound_2])
        single_list_y.extend(y1[low_bound_1:high_bound_1])
        single_list_y.extend(y2[low_bound_2:high_bound_2])
        percentile+=.1
        low_bound_1=high_bound_1
        low_bound_2=high_bound_2
    
    #for i in lst2:
     #   lst1.append(i)
    #for r in y2:
     #   y1.append(r)
    
    return single_list,single_list_y,result_type

    
#category_selector()
