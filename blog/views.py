from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic

from .models import Topic, Post


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_topics_list'

    def get_queryset(self):
        """Return the last five published topics"""
        return Topic.objects.order_by('-date_added')[:5]


class DetailView(generic.DetailView):
    model = Topic
    template_name = 'blog/detail.html'


class ResultsView(generic.DetailView):
    model = Topic
    template_name = 'blog/result.html'


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
