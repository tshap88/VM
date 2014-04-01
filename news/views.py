from django.shortcuts import render
from news.models import News

def Last5News(request):
    news = News.objects.all().order_by('date_pub')[:5]
    context = {'news': news}
    return render(request, 'index.html','support.html','about.html','blog.html','contact.html',context)

def NewsAll(request):
    news = News.objects.all().order_by('-date_pub')
    context = {'news': news}
    return render(request, 'news/news.html',context)

def SingleNews(request, new_id):
    news = News.objects.get(pk=new_id)
    context = {'news': news}
    return render(request, 'news/singlenews.html',context)

