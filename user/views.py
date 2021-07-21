from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.



def index(request):
    return HttpResponse('jjj')
    #return render(request,"index.html")
class TestView(View):
    def get(self,request):
        return HttpResponse("hello get")
    def posst(self,request):
        return HttpResponse('hello post')