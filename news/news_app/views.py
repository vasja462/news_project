from django.shortcuts import render
from .models import News
from django.views import View
# Create your views here.

class Index(View):
    def get(self, request):
        news = News.objects.all()
        categories = [category for category in News.CATEGORY]
        return render(request, 'news_app/index.html', context={'news': news,
                                                               'categories': categories})

class ShowNew(View):
    def get(self, request, id_new:int):
        new = News.objects.get(pk=id_new)
        return render(request, 'news_app/new.html', context={'new': new})


