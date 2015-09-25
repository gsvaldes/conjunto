from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.song_list, name="song_list"),
    url(r'^song/(?P<pk>[0-9]+)/$', views.song_detail, name='song_detail'),
    url(r'song/new/$', views.song_new, name='song_new'),
    url(r'^drafts/$', views.song_draft_list, name='song_draft_list'),
    url(r'^song/(?P<pk>[0-9]+)/edit/$', views.song_edit, name='song_edit'),
    url(r'^song/(?P<pk>[0-9]+)/publish/$', views.song_publish, name="song_publish"),
    url(r'^song/(?P<pk>[0-9]+)/remove/$', views.song_remove, name='song_remove'),
]