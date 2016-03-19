from django.shortcuts import render
from django.http import HttpResponse
import new1
def home(request):
    return render(request,'home.html')
def get(request):
    id=request.GET['id']
    ps=request.GET['ps']
    cookie=new1.myCookie(id,ps)
    page=cookie.open()
    return HttpResponse(page)
# Create your views here.
