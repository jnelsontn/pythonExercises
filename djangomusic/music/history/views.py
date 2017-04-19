from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import Artist
from .models import Song

# Create your views here.
def index(request):
    artist_list = Artist.objects.all()
    template = loader.get_template('history/index.html')
    context = {
    	'artist_list': artist_list,
    }
    return HttpResponse(template.render(context, request))

def artist(request, artist_id):
	artist = Artist.objects.get(pk=artist_id)
	template = loader.get_template('history/artist.html')
	context = {
		'artist': artist,
	}
	return HttpResponse(template.render(context, request))