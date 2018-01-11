from django.shortcuts import render, get_object_or_404
from . import index_2

# Create your views here.

def eval(request):

	eval_data = request.POST['evaluation']
	value = index_2.main(eval_data,6)

	if value == 1:
		value = "Positive"
	elif value == -1:
		value = "Negative"
	else:
		value = "Neutral"
	print(value)
	return render(request, 'evaluation/eval.html', {'content1':eval_data,'content2':value})




