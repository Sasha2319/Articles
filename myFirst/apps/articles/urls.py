from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('<int:article_id>/', views.detail, name='detail'),
    # path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment'),
]