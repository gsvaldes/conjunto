from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.song_list, name="song_list"),
    url(r'^song/(?P<pk>[0-9]+)/$', views.song_detail, name='song_detail'),
    url(r'song/new/$', views.song_new, name='song_new'),
]