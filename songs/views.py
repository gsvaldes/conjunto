from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import SongForm
from .models import Song


def song_list(request):
	songs = Song.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'songs/song_list.html', {'songs': songs})


def song_detail(request, pk):
	song = get_object_or_404(Song, pk=pk)
	return render(request, 'songs/song_detail.html', {'song': song})


@login_required
def song_new(request):
    if request.method =="POST":
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.author = request.user
            song.published_date = timezone.now()
            song.save()
            return redirect('songs.views.song_detail', pk=song.pk)
    else:      
        form = SongForm()
    return render(request, 'songs/song_edit.html', {'form': form})


@login_required
def song_draft_list(request):
	songs = Song.objects.filter(published_date__isnull=True).order_by('created_date')
	return render(request, 'songs/song_draft_list.html', {'songs': songs})


@login_required
def song_publish(request, pk):
	song = get_object_or_404(Song, pk=pk)
	song.publish()
	return redirect('songs.views.song_detail', pk=pk)


@login_required
def song_edit(request, pk):
	song = get_object_or_404(Song, pk=pk)
	if request.method == 'POST':
		form = SongForm(request.POST, instance=song)
		if form.is_valid():
			song = form.save(commit=False)
			song.author = request.user
			song.published_date = timezone.now()
			song.save()
			return redirect('songs.views.song_detail', pk=song.pk)
	else:
		form = SongForm(instance=song)
	return render(request, 'songs/song_edit.html', {'form': form})


@login_required
def song_remove(request, pk):
	song = get_object_or_404(Song, pk=pk)
	song.delete()
	return redirect('songs.views.song_list')