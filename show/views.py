#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
import re
import new1
def home(request):
    return render(request,'home.html')
def get(request):
    id=request.GET['id']
    ps=request.GET['ps']
    cookie=new1.myCookie(id,ps)
    page=cookie.open()
    if(page==-1):
        return render(request,'home.html',{'userkown':'用户名或密码错误'})
    else:
        request.session['username']=id
        request.session['password']=ps
    m=re.compile(r'<table name="" id="1" class="CourseFormTable" style="" >(.*?)</body>',re.S)
    body=re.search(m,page)
    return render(request,'show.html',{'main':body.group(1)})
def change(request):
    cookie=new1.myCookie(request.session['username'],request.session['password'])
    return render(request,'change.html',{'classlist':cookie.classtoclass()})
# Create your views here.
