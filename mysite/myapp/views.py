from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>This is Mysite ...HACKING will be dome Here</h1>')
