
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .forms import TestForm # forms.pyに記述したTestFormをimport


# def index(request):
#     return HttpResponse("Hello World fuck!")

def index(request):
    my_dict = {
      'insert_something':"views.pyのfucking insert_something部分です" ,
      'name':"morioka" ,
      'form':TestForm() ,
      'insert_forms':'default_value'
    }
    if (request.method == 'POST'):
      my_dict['insert_forms'] = '文字列:' + request.POST['text'] + '<br>整数型:' + request.POST['num']
      my_dict['form'] = TestForm(request.POST)
    return render(request,'webtestapp/index.html' , my_dict)
 
 
