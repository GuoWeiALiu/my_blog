from django.shortcuts import render

# Create your views here.
from mysite.models import Article


def index(request):
    articles = Article.objects.filter(status=1)
    return render(request, 'index.html', locals())
