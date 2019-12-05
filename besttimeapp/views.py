from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """トップページ"""
    context = {
        'name': 'Welcome to Best Time Manage App',
    }
    return render(request, 'besttimeapp/index.html') #, context)

def about(request):
    """ about アバウトページ"""
    return render(request, 'about.html')

def info(request):
    """ info インフォページ"""
    return render(request, 'info.html')

def signup(request):
    """ signup サインアップページ"""
    return render(request, 'signup.html')

def getbest(request, name):
    return HttpResponse("Your best time is %s." % name)
