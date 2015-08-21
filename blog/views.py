from django.shortcuts import render, get_object_or_404
from .models import Topic, Post


def index(request):
    latest_topics_list = Topic.objects.order_by('-date_added')[:5]

    context = {
        'latest_topics_list': latest_topics_list,
    }

    return render(request, 'blog/index.html', context)


def detail(request, topic_id):
    topic = get_object_or_404(Topic, pk = topic_id)
    latest_posts_list = Post.objects.filter(topic = topic_id)

    context = {
        'topic': topic,
        'latest_posts_list': latest_posts_list,
    }

    return render(request, 'blog/detail.html', context)