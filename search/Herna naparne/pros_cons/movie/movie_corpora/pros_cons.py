import csv
import general

file = "C:\\Users\\Rajesh\\Desktop\\Requests\\pros_cons\\movie\\movie_corpora\\positive.txt"
fname = 'pos1.csv'
save = open(fname,'a')
read = open(file,'r').readlines()
#cons = []
#y_cons = []
count = 0
for i in read:
    clan = general.cleanhtml(i)
    clean1 = clan.replace(",",".")
    clean2 = clean1.replace("\n"," , 1"+'\n')
    save.write(clean2)
    #cons.append(clean2)
    #y_cons.append("1")
    count += 1
#save.write(str(cons))
#save.write("\n" + str(y_cons))
save.close()
print('count:',count)
#print(len(cons))
#print(len(y_cons))
