from django.shortcuts import render
from .models import Article, Comment
from django.http.response import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .forms import CommentForm
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    latest_articles = Article.objects.order_by('-pub_date')
    return render(request, 'articles/list.html', {'latest_articles':latest_articles})

@csrf_exempt
def detail(request, article_id):
    a = Article.objects.get(id=article_id)
    form = CommentForm()
    data = {}
    if request.is_ajax():
        data['comment_author'] = request.POST.get("comment_author")
        data['comment_text'] = request.POST.get("comment_text")
        a.comment_set.create(comment_author=data['comment_author'], comment_text=data['comment_text'])
        return JsonResponse(data)
    article = Article.objects.get(id = article_id)
    comments_list = article.comment_set.all()
    comments = reversed(comments_list)
    # return HttpResponse("Hello")
    return render(request, 'articles/detail.html', {'article': article, 'comments':comments, 'form': form, })




