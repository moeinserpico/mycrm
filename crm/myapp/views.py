from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!")

def index(request):
    return HttpResponse("<p><h1>Hello</h1>this is simple index</p>")


