
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .forms import TestForm # forms.pyに記述したTestFormをimport
from .forms import InfoModelFormAdd
from .models import InfoModelForm
from .models import SearchModelForm
from django.shortcuts import redirect

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
 

def info(request):
    infodata = InfoModelForm.objects.all()
    header = ['ID','名前','メール','性別','部署','社歴','作成日','']
    my_dict2 = {
        'title':'テスト',
        'val':infodata,
        'header':header,
    }
    return render(request, 'webtestapp/info.html',my_dict2)

def create(request):
    if (request.method == 'POST'):
        obj = InfoModelForm()
        info = InfoModelFormAdd(request.POST, instance=obj)
        info.save()
        return redirect(to='/info')
    modelform_dict = {
        'title':'modelformテスト',
        'form':InfoModelFormAdd(),
    }
    return render(request, 'webtestapp/create.html', modelform_dict)


def update(request, num):
    obj = InfoModelForm.objects.get(id=num)
    # POST送信されていたら
    if (request.method == 'POST'):
        info = InfoModelFormAdd(request.POST, instance=obj)
        info.save()
        header = ['ID','名前','メール','性別','部署','社歴','作成日','']
        return redirect(to='/info')
    update_dict = {
        'title':'登録情報更新画面',
        'id':num,
        'form':InfoModelFormAdd(instance=obj),
    }
    return render(request, 'webtestapp/update.html',update_dict)

def delete(request, num):
    obj = InfoModelForm.objects.get(id=num)
    if (request.method == 'POST'):
        obj.delete()
        return redirect(to='/info')
    delete_dict = {
        'title':'削除確認',
        'id':num,
        'obj':obj,
    }
    return render(request, 'webtestapp/delete.html',delete_dict)

def search(request):
    infodata = InfoModelForm.objects.all()
    if not request.POST.get('a') : # for ID
      pass
    else :
      searcha = request.POST.get('a')
      infodata = InfoModelForm.objects.filter(id=request.POST.get('searcha'))
    if not request.POST.get('b') : # for NAME
      pass
    else :
      searchb = str(request.POST.get('b'))
      infodata = infodata.filter(name__contains=searchb)
    if not request.POST.get('c') : # for E-MAIL
      pass
    else :
      infodata = infodata.filter(mail__contains=request.POST.get('c'))
    if not request.POST.get('d') : # for GENDER
      pass
    else :
      if request.POST.get('d') == 0 :
        searchd = False
      else :
        searchd = True
      infodata = infodata.filter(gender=request.POST.get('c'))
    if not request.POST.get('e') : # for DEPARTMENT
      pass
    else :
      infodata = infodata.filter(department__contains=request.POST.get('e'))
    if not request.POST.get('f') : # for YEAR
      pass
    else :
      searchf = int(request.POST.get('f'))
      infodata = infodata.filter(year=request.POST.get('f'))
    header = ['ID','名前','メール','性別','部署','社歴','作成日','']
    my_dict2 = {
        'title':'テスト',
        'val':infodata,
        'header':header,
    }
    return render(request, 'webtestapp/search.html',my_dict2)



