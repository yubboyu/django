
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello World fuck!")

def index(request):
    return render(request,'webtestapp/index.html')
 
 
