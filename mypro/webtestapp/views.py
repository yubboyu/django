
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello World fuck!")

def index(request):
    my_dict = {
      'insert_something':"views.pyのfucking insert_something部分です" ,
      'name':"morioka"
    }
    return render(request,'webtestapp/index.html' , my_dict)
 
 
