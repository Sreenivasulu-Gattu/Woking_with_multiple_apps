from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def willi(request):
    return HttpResponse('<h1>Williom is playing now..</h1>')

def ravi(request):
    return HttpResponse('<h1>Ravi will going to play later..</h1>')
