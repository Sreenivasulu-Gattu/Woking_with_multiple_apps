from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def msd(request):
    return HttpResponse('<h1>Mahindra Sing Dhoni</h1>')

def kohli(request):
    return HttpResponse('<h1>King kohli reached 50th century..</h1>')