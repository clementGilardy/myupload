from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import RequestContext

def home (request):
    return render(request, 'index.html')

def documents (request):
    return render(request, 'document.html')

