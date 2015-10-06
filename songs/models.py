from django.db import models
from django.utils import timezone

class Song(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
    	self.published_date = timezone.now()
    	self.save()


    def __unicode__(self):
    	return self.title


class Media(models.Model):
    song = models.ForeignKey(Song, related_name='videos')
    url = models.URLField()
    title = models.CharField(max_length=200)

    def __unicode__(self):
    	return self.title

    class Meta:
    	abstract = True


class Video(models.Model):
    song = models.ForeignKey(Song, related_name='videos')
    url = models.URLField()
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title


class MP3(models.Model):
	song = models.ForeignKey(Song, related_name='mp3s')
	url = models.URLField()
	title = models.CharField(max_length=200)

	def __unicode__(self):
		return self.title

