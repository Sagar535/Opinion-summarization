import csv

file = "C:\\Users\\Rajesh\\Desktop\\Requests\\pros_cons\\cons.csv"

read = open(file,'r').readlines()
count = 0
with open(file) as csvfile:
    readCSV = csv.reader(csvfile)
    for i in readCSV:
        print(i)
