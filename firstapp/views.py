from django.shortcuts import render
from django.http import HttpResponse
# First Request
# def index(request):
# 	return HttpResponse("Hello World")

# Second Request
from .forms import StudentForm

def index(request):
	if request.method=='POST':
		form = StudentForm(request.POST)
		if form.is_valid:
			form.save()
	form = StudentForm()
	return render(request,'index.html',{'form':form})
