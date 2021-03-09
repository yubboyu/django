
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .forms import TestForm # forms.pyに記述したTestFormをimport
from .forms import InfoModelFormAdd
from .models import InfoModelForm
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

def search(request , a , b , c , d , e , f , g ):
    infodata = InfoModelForm.objects.filter()
    header = ['ID','名前','メール','性別','部署','社歴','作成日','']
    my_dict2 = {
        'title':'テスト',
        'val':infodata,
        'header':header,
    }
    return render(request, 'webtestapp/info.html',my_dict2)



