from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.views import generic

from .models import Topic, Comment
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'forum/index.html'
    context_object_name = 'latest_topic_list'

    def get_queryset(self):
        return Topic.objects.order_by('-pub_date')[:5]

class TopicView(generic.DetailView):
    model = Topic
    template_name = 'forum/topic.html'

def add_topic(request):
    if (request.POST['title']):
        topic = Topic(
            pub_date=timezone.now(),
            title_text=request.POST['title'],
            author_id=request.user.id
        )
        topic.save()
        return HttpResponseRedirect(reverse('forum:index'))

def comments(request, topic_id, comment_id):
    return HttpResponse("You're looking at topic %s and comment %s" % topic_id, comment_id)

def add_comment(request, topic_id):
    if (request.POST['comment']):
        comment = Comment(
            topic_id=topic_id,
            pub_date=timezone.now(),
            comment_text=request.POST['comment'],
            author_id=request.user.id
        )
        comment.save()
        return HttpResponseRedirect(reverse('forum:topics', args=(topic_id,)))