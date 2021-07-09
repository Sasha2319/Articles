from django.db import models
import datetime
from django.utils import timezone
import django
# Create your models here.

class Article(models.Model):
    article_title = models.CharField('название статьи', max_length=200, default='')
    article_text = models.TextField('текст статьи', default='')
    pub_date = models.DateTimeField('дата публикации', auto_now_add=True)
    author_name = models.CharField('имя автора', max_length=55, default='')
    article_image = models.ImageField(upload_to='img', default='', blank=True)

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_author = models.CharField('имя автора', max_length=50)
    comment_text = models.TextField('текст комментария')
    cDate = models.DateTimeField('дата публикации', auto_now_add=True)


    def __str__(self):
        return self.comment_author
