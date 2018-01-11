import csv
import time
from bs4 import BeautifulSoup
from . import general
import os

def get_question_link(link4quora):
  """
     Returns complete link for quora
  """
  question_link = soup.find('a', attrs = {'class' : 'question_link'})
  return 'http://www.quora.com' + question_link.get('href')

def obtain_url(search_keyword):
  #to get link from search_keyword
  url = 'https://www.quora.com/search?q=' + search_keyword
  return url,search_keyword

def save_links_quora(soup,search_keyword):
  '''
   to save links
  '''
  fname = 'urls_' + search_keyword + '.csv'
  path = os.getcwd() + '/search/Scrapped/URLs'
  file_name = os.path.join(path,fname)
  saveFile = open(file_name,'a')
  for url in soup.find_all('a',attrs = {'class' : 'question_link'}):
    quora_link = str(url.get('href'))
    quora_link = quora_link.replace('/',' ')
    quora_link = quora_link.split()
    if (quora_link[0] != 'unanswered'):
      file = 'https://www.quora.com' + str(url.get('href')) + "\n"
      saveFile.write(file)
  saveFile.close()


