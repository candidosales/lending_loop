from django.urls import path

from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/<int:topic_id>/', views.topics, name='topics'),
    path('<int:comment_id>/', views.comments, name='comments')
]