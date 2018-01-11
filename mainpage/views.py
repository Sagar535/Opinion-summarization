from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .import links
from .import general,pages
import json, random

# Create your views here.

def index(request):
	return render(request, 'mainpage/home.html')

def contact(request):
	return render(request,'mainpage/contact.html', {'content':['If you want to contact IRUSh mail at:','070bct535@ioe.edu.np',
		'070bct535@ioe.edu.np','070bct535@ioe.edu.np','070bct535@ioe.edu.np']})


	
def bar(request):
	return render(request, 'mainpage/bar.html')

def summary(request):
    values = ["happy", "sad", "awesome", "good", "bad", "nice" , "okay"]
    frequency = [10,20,30,40,50,60,70]
    # x = []
    # for i in range(0,len(values)):
    #     x.append(str(i))

    # val = dict(zip(x,values))  
    # val['last'] = len(values) 

    final = []
    j = 0
    for i in values:
        f = frequency[j];
        final.append(i + "(" + str(f) +")")
        j = j+1 

    val  = {"emotions" : final, "freq" : frequency}

    return render(request,'mainpage/wordCloud.html',val)

def evaluation(request):
    eval_data = request.POST['evaluation']
    temp = random.randint(1,9)
    if temp%3==0:
        value = "POSITIVE"
    elif temp%3==1:
        value = "NEGATIVE"
    else:
        value = "Neutral"

    return render(request,'mainpage/evaluation.html',{'content1':eval_data, 'content2':value})

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