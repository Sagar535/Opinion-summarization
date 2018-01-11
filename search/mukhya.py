from . import index
from . import general
#import mainop

def operation(Keyword):
    global search_keyword
    search_keyword = Keyword
    search_keyword = general.ReFormatt(search_keyword)
    index.main1(search_keyword)
    #index_2.mainop(search_keyword)

# operation()
