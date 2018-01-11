import csv

from django.shortcuts import render
from . import mukhya
from . import main_UI

def search(request):
	keyword = request.POST['text']
	choosed = request.POST.get('choice')
	
	print(choosed)

	mukhya.operation(keyword)

	#split and join to transfrom iphone 7 to iphone+7
	temp = keyword.split(" ")
	keyword_processed = "+".join(temp)

	pos_per, neg_per, pos_list, neg_list = main_UI.main(keyword_processed)
	# main_UI.main(keyword_processed, 1)

	pos_per *=100
	neg_per *= 100

	# ,{'positive':pos_per, 'negative':neg_per}

	print(pos_per)
	print(neg_per)

	with open ('comments.csv','w') as csvfile:
		fieldnames = ['Positive_words', 'Negative_words']
		writer = csv.DictWriter(csvfile, fieldnames =fieldnames)

		writer.writeheader()
		for i in range(len(pos_list)):
			writer.writerow({'Positive_words':pos_list[i], 'Negative_words':neg_list[i]})

	with open('percent.csv','w') as csvfile:
		fieldnames = ['Positive', 'Negative']
		writer = csv.DictWriter(csvfile,fieldnames = fieldnames)
		writer.writeheader()
		writer.writerow({'Positive':pos_per , 'Negative':neg_per})
	
	if choosed == "WordCloud":
		return render(request,'search/wordCloud.html',{'positive':pos_list, 'negative':neg_list})

	else:
		return render(request, 'search/bar.html',{'positive':pos_per, 'negative':neg_per})

def bar(request):
	with open('percent.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			pos_per= row['Positive']
			neg_per = row['Negative']

	print(pos_per)
	print(neg_per)

	return render(request, 'search/bar.html',{'positive':pos_per, 'negative':neg_per})

def wordCloud(request):
	with open('comments.csv') as csvfile:
		reader = csv.DictReader(csvfile)
		pos_list = []
		neg_list = []
		for row in reader:
			pos_list.append(row['Positive_words'])
			neg_list.append(row['Negative_words'])

	print(pos_list)
	print(neg_list)
	return render(request,'search/wordCloud.html',{'positive':pos_list, 'negative':neg_list})

