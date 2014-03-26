from django.shortcuts import render

# Create your views here.
#from app1.models import App1,Choice
from news.models import News


def index(request):
    news = News.objects.all().order_by('date_pub')[:5]
    context = {'news': news}
    return render(request, 'index.html', context)


def support(request):
    context = {'support': support}
    return render(request, 'support.html', context)


def about(request):
    context = {'about': about}
    return render(request, 'about.html', context)


def blog(request):
    context = {'blog': blog}
    return render(request, 'blog.html', context)


def contact(request):
    context = {'contact': contact}
    return render(request, 'contact.html', context)
