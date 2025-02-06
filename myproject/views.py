#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse(" This is my first Django HomePage")
    return render(request, 'home.html')

def about(request):
    #return HttpResponse("This is my About page")
    return render(request, 'about.html')