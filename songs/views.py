from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Song

def song_list(request):
	songs = Song.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'songs/song_list.html', {'songs': songs})

def song_detail(request, pk):
	song = get_object_or_404(Song, pk=pk)
	return render(request, 'songs/song_detail.html', {'song': song})