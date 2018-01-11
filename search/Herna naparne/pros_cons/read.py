import csv

file = "C:\\Users\\Rajesh\\Desktop\\Requests\\pros_cons\\cons.csv"
count = 0
with open(file) as csvfile:
    readCSV = csv.reader(csvfile)
    lst = list(readCSV)
    print(lst[0])
    '''
    for row in readCSV:
        for i in row:
            print(i)
            count += 1
            if count>10:
                break
'''
        
