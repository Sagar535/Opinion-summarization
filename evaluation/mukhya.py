import index
import general
import index_2

def operation():
    global search_keyword
    search_keyword = input('Enter a Keyword:')
    search_keyword = general.ReFormatt(search_keyword)
    index.main1(search_keyword)
    index_2.mainop(search_keyword)
    

operation()
