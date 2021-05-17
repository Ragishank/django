from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Testfun(request):

    return HttpResponse('hi there')
def Htmlfun(request):
    return render(request,'test.html')
    
def newfun(request):
    return render(request,'new.html')