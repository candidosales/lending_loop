from django.urls import path

from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('topics', views.add_topic, name='add_topic'),
    path('topics/<uuid:pk>/', views.TopicView.as_view(), name='topics'),
    path('topics/<uuid:topic_id>/comment/', views.add_comment, name='add_comment'),

]