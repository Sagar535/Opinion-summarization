import general
import urllib.request
import urllib.parse
import io
from bs4 import BeautifulSoup

url = "C:\\Users\\Rajesh\\Desktop\\Requests\\nayanaya.html"
soup = BeautifulSoup(open(url,encoding='utf-8'),"lxml")
final_file = open('final_maybe_nayanaya_finale.txt','a')
for parg in soup.find_all('div',attrs={'class':'inline_editor_content'}):
    for par in parg.find_all('span',attrs={'class':'rendered_qtext'}):
        pgh=general.cleanhtml(str(par))
        final_file.write(pgh)
        print(pgh)
final_file.close()
