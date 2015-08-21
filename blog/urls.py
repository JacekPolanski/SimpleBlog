from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /blog/
    url(r'^$', views.index, name='index'),
    # ex: /blog/5/
    url(r'^(?P<topic_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /blog/5/vote
    url(r'^(?P<topic_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # ex: /blog/5/results
    url(r'^(?P<topic_id>[0-9]+)/results/$', views.results, name='results'),
]