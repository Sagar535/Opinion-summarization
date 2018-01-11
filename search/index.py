from . import links
from . import general
from . import pages
#import index_2

def entry(search_keyword):
    '''
    To get about 10 must discussed questions about the keyword in Quora
    '''
    try:
        url,search_keyword = links.obtain_url(search_keyword)
        print('URL Done')
        soup = general.obtain_soup(url)
        links.save_links_quora(soup,search_keyword)
    except Exception as e:
        print(str(e))
    
def main1(search_keyword):
    entry(search_keyword)# For getting top question links
    print('Soup  Done')
    pages.pages_1(search_keyword) # To get some text about the keyword
    print('Txt Done')
    '''
    Text badauna 6 bhane pages.py ma gayera if(count>(number)) change garnu
    '''
