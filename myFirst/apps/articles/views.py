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
    comments_list = article.comment_set.all()
    comments = reversed(comments_list)
    return render(request, 'articles/detail.html', {'article':article, 'comments':comments,})

def leave_comment(request, article_id):
    if request.POST.get('name') and request.POST.get('text'):
        a = Article.objects.get(id=article_id)
        a.comment_set.create(comment_author=request.POST.get('name'), comment_text=request.POST.get('text'))
    b = '/' + str(article_id)
    return HttpResponseRedirect(b)



