from django.shortcuts import render


def index(request):
    context = {}
    
    return render(request, './index.html', context)


def style(request):
    context = {}
    
    return render(request, './style.css', context)
