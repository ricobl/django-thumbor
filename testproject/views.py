from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'index.html', context)
