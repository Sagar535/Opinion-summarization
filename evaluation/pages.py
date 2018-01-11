import csv
import time
import io
import links
import general
import os

def quora_extraction_fromLink(search_keyword):
    total_files = []
    path = os.getcwd() + '/Scrapped/URLs/'
    file_name = path + 'urls_' + search_keyword + '.csv'
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
        fname = 'final_'+ search_keyword + '.txt'
        path = os.getcwd() + '/Scrapped/Texts'
        file_name = os.path.join(path,fname)
        final_file = io.open(file_name,'a',encoding='utf-8')
        
        for parg in quora_soup.find_all('div',attrs={'class':'ExpandedQText ExpandedAnswer'}):
            for par in parg.find_all('span',attrs={'class':'rendered_qtext'}):
                pgh=general.cleanhtml(str(par))
                pgh1 = pgh + '\n' + '\n'
                final_file.write(pgh1)
                #print(pgh)
        final_file.close()
        count = count + 1
        if (count>2):
            break
                
    
        #time.sleep(5)
#pages_1('neil+armstrong')
