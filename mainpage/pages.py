import csv
import time
import io
from .import links, general

def quora_extraction_fromLink(search_keyword):
    total_files = []
    file_name = 'urls_' + search_keyword + '.csv'
    with open(file_name) as csvfile:
        readCSV = csv.reader(csvfile)
        for row in readCSV:
            y=row[0]
            total_files.append(y)
    return total_files

def pages_1(search_keyword):
    total_files_fromQuora = quora_extraction_fromLink(search_keyword)
    count = 0
    for i in total_files_fromQuora:
        quora_soup = general.obtain_soup(i)
        file_name = 'final_'+ search_keyword + '.txt'
        final_file = open(file_name,'a')
        
        for parg in quora_soup.find_all('div',attrs={'class':'ExpandedQText ExpandedAnswer'}):
            for par in parg.find_all('span',attrs={'class':'rendered_qtext'}):
                pgh=general.cleanhtml(str(par))
                pgh1 = pgh + '\n' + '\n'
                final_file.write(pgh1)
                #print(pgh)
        final_file.close()
        count = count + 1
        if (count>1):
            break
                
    
        #time.sleep(5)
#pages_1('neil+armstrong')
