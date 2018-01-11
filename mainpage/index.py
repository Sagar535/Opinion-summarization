from .import links
from .import general,pages


search_keyword=''

def entry(keyword):
#To get about 10 must discussed questions about the keyword in Quora 
    try:
        global search_keyword  
        search_keyword = keyword
        '''
          Yo enter a keyword lai input liyera submit garne banau hai
        '''
        #search_keyword = input('Enter a Keyword:')
        url,search_keyword = links.obtain_url(search_keyword)
        soup = general.obtain_soup(url)
        links.save_links_quora(soup,search_keyword)
    except Exception as e:
        print(str(e))
    
def main(keyword):
    global search_keyword 
    search_keyword = keyword
    entry(search_keyword)# For getting top question links
    pages.pages_1(search_keyword) # To get some text about the keyword
    '''
    Text badauna 6 bhane pages.py ma gayera if(count>(number)) change garnu
    '''

#main()
