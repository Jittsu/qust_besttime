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
    return render(request, 'besttimeapp/about.html')

def info(request):
    """ info インフォページ"""
    return render(request, 'besttimeapp/info.html')

def signup(request):
    """ signup サインアップページ"""
    return render(request, 'besttimeappsignup.html')

def get_alldata(request):
    """ 全データの取得 """
    return render(request, 'besttimeapp/showall.html')

def get_best(request, name):
    return HttpResponse("Your best time is %s." % name)
