import pprint
from django.http import Http404
from django.shortcuts import render
from .models import Topic, Post


def index(request):
    latest_topics_list = Topic.objects.order_by('-date_added')[:5]

    context = {
        'latest_topics_list': latest_topics_list,
    }

    return render(request, 'blog/index.html', context)


def detail(request, topic_id):
    try:
        topic = Topic.objects.get(id = topic_id)
    except Topic.DoesNotExist:
        raise Http404("Topic nie istnieje")

    latest_posts_list = Post.objects.filter(topic = topic_id)

    context = {
        'topic': topic,
        'latest_posts_list': latest_posts_list,
    }

    return render(request, 'blog/detail.html', context)