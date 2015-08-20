from django.http import HttpResponse
from django.shortcuts import render
from .models import Topic


def index(request):
    latest_topics_list = Topic.objects.order_by('-date_added')[:5]

    context = {
        'latest_topics_list': latest_topics_list,
    }

    return render(request, 'blog/index.html', context)


def detail(request, topic_id):
    return HttpResponse("Topic: %s." % topic_id)