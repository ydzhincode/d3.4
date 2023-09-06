from django.urls import path
from NewsPaper import views

urlpatterns = [
    path('', views.index, name='index', ),
    path('news/', views.post_list, name='post_list', ),
    path('news/<int:post_id>/', views.post_show, name='post_show', ),
]
