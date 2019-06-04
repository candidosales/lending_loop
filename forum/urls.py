from django.urls import path

from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('topics', views.add_topic, name='add_topic'),
    path('topics/<int:pk>/', views.TopicView.as_view(), name='topics'),
    path('topics/<int:topic_id>/comment/', views.add_comment, name='add_comment'),

]