from django.shortcuts import render
from .models import Article, Comment
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    latest_articles = Article.objects.order_by('-pub_date')
    return render(request, 'articles/list.html', {'latest_articles':latest_articles})

def detail(request, article_id):
    article = Article.objects.get(id = article_id)
    return render(request, 'articles/detail.html', {'article':article})

def leave_comment(request, article_id):
    a = Article.objects.get(id=article_id)
    a.comment_set.create(comment_author=request.POST.get('name'), comment_text=request.POST.get('text'))
    b = '/' + str(article_id)
    return HttpResponseRedirect(b)



