from django.http import HttpResponse
from django.shortcuts import render
from hello import daoemp
from django.http.response import JsonResponse
from hello.daoemp import DaoEmp

def hello(request):
    return HttpResponse("hello django")

def param(request):
    a = request.POST.get("a", "babo")
    if request.method == 'POST':
        return HttpResponse("param : " + a)
    return HttpResponse("param : " + a)


def dispa(request):
    a = "aaa"
    b = ["홍길동", "전우치", "이순신"]
    c = [
        {'e_id' : '1', 'e_name' : '홍길동', 'sex' : 'm', 'addr' : '대전시'},
        {'e_id' : '2', 'e_name' : '전우치', 'sex' : 'f', 'addr' : '대구시'},
        {'e_id' : '3', 'e_name' : '이순신', 'sex' : 'm', 'addr' : '아산시'}
        ]
    
    context = { 
        'a' : a, 
        'b' : b, 
        'c' : c
    }
    return render(request, "dispa.html", context)



def emp(request):
    mylist = daoemp.DaoEmp().myselect()
    # listjson = []
    # for mem in mylist:
    #     listjson.append({'e_id' : mem[0], 'e_name' : mem[1], 'sex' : mem[2], 'addr' : mem[3]})
    context = { 'mylist' : mylist}
    return render(request, "emp.html", context)

def ajax(request):
    a= request.POST['a']
    print("a", a)
    context={'msg': 'ok'}
    return JsonResponse(context)

def ajax_insert(request):
    e_id= request.POST['e_id']
    e_name= request.POST['e_name']
    sex= request.POST['sex']
    addr= request.POST['addr']
    
    de=DaoEmp()
    msg = "ng"
    
    cnt = de.myinsert(e_id, e_name, sex, addr)
    if cnt == 1 : 
        msg = "ok"
    context={'msg': msg}
    return JsonResponse(context)

def ajax_update(request):
    e_id= request.POST['e_id']
    e_name= request.POST['e_name']
    sex= request.POST['sex']
    addr= request.POST['addr']
    
    de=DaoEmp()
    msg = "ng"
    
    cnt = de.myupdate(e_id, e_name, sex, addr)
    if cnt == 1 : 
        msg = "ok"
    context={'msg': msg}
    return JsonResponse(context)


def ajax_delete(request):
    e_id= request.POST['e_id']
    
    de=DaoEmp()
    msg = "ng"
    
    cnt = de.mydelete(e_id)
    if cnt == 1 : 
        msg = "ok"
    context={'msg': msg}
    return JsonResponse(context)

