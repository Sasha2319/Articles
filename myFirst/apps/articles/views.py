from django.shortcuts import render
from .models import Article, Comment
from django.http.response import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .forms import CommentForm
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.utils import timezone
import datetime
import pytz
import locale
import time
from myFirst.settings import STATIC_URL
from django.db.models import Q


# Create your views here.
def index(request):
    return HttpResponseRedirect('home')

def home(request):
    latest_articles = Article.objects.order_by('-pub_date')
    if request.GET.get("q"):
        queryset = Article.objects.all()
        q = request.GET.get("q").lower()
        if q:
            a = queryset.filter(Q(article_title__icontains=q) | Q(article_text__icontains=q))
            marksText = {}
            marksTitle = {}
            print(a)
            for qset in a:
                i = qset.article_text.find(q)
                if i > -1:
                    print(i)
                    marksText[qset.id] = i

            for qset in a:
                i = qset.article_title.find(q)
                if i > -1:
                    print(i)
                    marksTitle[qset.id] = i

            print(marksText)
            print(marksTitle)

            if a:
                return render(request, 'articles/list.html', {'latest_articles': a, 'static': STATIC_URL, 'error': False, 'script': True, 'mText': marksText, 'mTitle': marksTitle, 'q': q, })
            else:
                return render(request, 'articles/list.html', {'latest_articles': latest_articles, 'static': STATIC_URL, 'error': True,})
    return render(request, 'articles/list.html', {'latest_articles':latest_articles, 'static': STATIC_URL, 'error': False,})


@csrf_exempt
def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        return render(request, 'articles/404.html', {'static': STATIC_URL, })
    form = CommentForm()
    data = {}
    if request.is_ajax():
        data['comment_author'] = request.POST.get("comment_author")
        data['comment_text'] = request.POST.get("comment_text")
        locale.setlocale(locale.LC_TIME, "ru_RU")
        data['cDate'] = time.strftime("%d %B %Y г. %H:%M")
        a.comment_set.create(comment_author=data['comment_author'], comment_text=data['comment_text'])
        return JsonResponse(data)

    article = Article.objects.get(id = article_id)
    comments_list = article.comment_set.all()
    comments = reversed(comments_list)
    # return HttpResponse("Hello")
    return render(request, 'articles/detail.html', {'article': article, 'comments':comments, 'form': form, 'static': STATIC_URL, })

def about(request):
    return render(request, 'articles/about.html', {'static': STATIC_URL})

def create(request):
    return render(request, 'base.html', {'static': STATIC_URL})

def edit(request):
    return render(request, 'base.html', {'static': STATIC_URL})

def report(request):
    return render(request, 'base.html', {'static': STATIC_URL})



# @csrf_exempt
# def search(request):
#     queryset = Article.objects.all()
#     q = request.GET.get("q")
#     if q:
#         # Если 'q' в GET запросе, фильтруем кверисет по данным из 'q'
#         a = queryset.filter(Q(article_title__icontains=q) | Q(article_text__icontains=q))
#         return render(request, 'articles/list.html', {'latest_articles':a, 'static': STATIC_URL,})
#     # return queryset
#     return HttpResponse("Hello")

