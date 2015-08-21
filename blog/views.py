from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Topic, Post


def index(request):
    latest_topics_list = Topic.objects.order_by('-date_added')[:5]

    context = {
        'latest_topics_list': latest_topics_list,
    }

    return render(request, 'blog/index.html', context)


def detail(request, topic_id):
    topic = get_object_or_404(Topic, pk = topic_id)

    context = {
        'topic': topic,
    }

    return render(request, 'blog/detail.html', context)


def vote(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)

    try:
        selected_post = topic.post_set.get(pk=request.POST['post'])
    except (KeyError, Post.DoesNotExist):
        return render(request, 'blog/detail.html', {
            'topic': topic,
            'error_message': "Nie zaznaczyłeś posta",
        })
    else:
        selected_post.votes += 1
        selected_post.save()

    return HttpResponseRedirect(reverse('blog:results', args=(topic.id,)))


def results(request, topic_id):
    topic = get_object_or_404(Topic, pk = topic_id)

    return render(request, 'blog/result.html', {'topic': topic})
