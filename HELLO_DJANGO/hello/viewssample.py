from django.http import HttpResponse
from django.shortcuts import render
from hello import daosample
from django.http.response import JsonResponse
from hello.daosample import DaoSmp


def smp(request):
    de=DaoSmp()
    smpList = de.myselect()
    
    context = {'smpList' : smpList}
    return render(request, "sample.html", context)

def smp_insert(request):
    col01= request.POST['col01']
    col02= request.POST['col02']
    col03= request.POST['col03']
    
    de=DaoSmp()
    msg = "ng"
    
    cnt = de.myinsert(col01, col02, col03)
    if cnt == 1 : 
        msg = "ok"
    context={'msg': msg}
    return JsonResponse(context)

def smp_update(request):
    col01= request.POST['col01']
    col02= request.POST['col02']
    col03= request.POST['col03']

    de=DaoSmp()
    msg = "ng"
    
    cnt = de.myupdate(col01, col02, col03)
    if cnt == 1 : 
        msg = "ok"
    context={'msg': msg}
    return JsonResponse(context)


def smp_delete(request):
    col01= request.POST['col01']
    
    de=DaoSmp()
    msg = "ng"
    
    cnt = de.mydelete(col01)
    if cnt == 1 : 
        msg = "ok"
    context={'msg': msg}
    return JsonResponse(context)


def axios_sync(request):
    col01= request.GET.get("col01", -1)
    icol01 = int(col01)
    icol01 += 1
    context = {'col01' : icol01}
    return JsonResponse(context)

def ajax_sync(request):
    col01= request.POST["col01"]
    icol01 = int(col01)
    icol01 += 1
    context = {'col01' : icol01}
    return JsonResponse(context)

