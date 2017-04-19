from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /history/
    url(r'^$', views.index, name='index'),
    # ex: /history/5/
    url(r'^(?P<artist_id>[0-9]+)/$', views.artist, name='artist'),
]