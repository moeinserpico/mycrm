from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!")

def index(request):
    context={'name':'moein sarvi','age':36,'title':'developer'}
    return render(request,'myapp/index.html',context)

