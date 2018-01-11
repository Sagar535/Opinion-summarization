import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import re


#To insert + ie for formatting
def ReFormatt(textword):
    textword= textword.replace(' ','+')
    return textword

#to obtain soup
def obtain_soup(url):
  headers = {}
  headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
  req = urllib.request.Request(url,headers=headers)
  resp = urllib.request.urlopen(req)
  respData = resp.read()
  soup = BeautifulSoup(respData,'lxml')
  return soup

#to obtain only numerical value out of string
def try_cast_int(s):
  try:
    pattern = re.compile(r'([0-9]+(\.[0-9]+)*[ ]*[Kk])|([0-9]+)')
    raw_result = re.search(pattern, s).groups()
    if raw_result[2] != None:
      return int(raw_result[2])
    elif raw_result[1] == None:
      raw_result = re.search(r'([0-9]+)', raw_result[0])
      return int(raw_result.groups()[0]) * 1000
    else:
      raw_result = re.search(r'([0-9]+)\.([0-9]+)', raw_result[0]).groups()
      return int(raw_result[0]) * 1000 + int(raw_result[1]) * 100
  except:
    return s

#to obtain rawhtml without html tags
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def file_name(search_keyword):
    file = 'final_'+ search_keyword + '.txt'
    return file

def token2sent(intermed):
    paragraph = ''
    pardoc = []
    for tpar in intermed:
        paragraph = ''
        for i in tpar:
            paragraph += str(i) + " "
        pardoc.append(paragraph)
    return pardoc

def cat4input(list_doc):
    paragraph = ''
    for each in list_doc:
        paragraph += str(each) + ' '
    return paragraph
    

#raj = ['I m Rajesh.','And you are ','nobody']
#paradoc = token2sent(raj)
#print(paradoc)

