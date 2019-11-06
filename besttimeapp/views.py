from django.shortcuts import render

def index(request):
    """トップページ"""
    context = {
        'name': 'Welcome to Best Time Manage App',
    }
    return render(request, 'index.html') #, context)

def about(request):
    """ about アバウトページ"""
    return render(request, 'about.html')

def info(request):
    """ info インフォページ"""
    return render(request, 'info.html')
