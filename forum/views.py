from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Topic
# Create your views here.
def index(request):
    latest_topic_list = Topic.objects.order_by('-pub_date')[:5]
    context = { 'latest_topic_list': latest_topic_list }
    return render(request, 'forum/index.html', context)

def topics(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    return render(request, 'forum/topic.html', {' topic': topic })

def comments(request, topic_id, comment_id):
    return HttpResponse("You're looking at topic %s and comment %s" % topic_id, comment_id)