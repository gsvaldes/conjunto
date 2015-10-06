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
    VIDEO = 'VID'
    MP3 = 'MP3'
    PDF = 'PDF'
    MEDIA_CHOICES = (
        (VIDEO, 'Video'),
        (MP3, 'MP3'),
        (PDF, 'PDF'),
    )

    song = models.ForeignKey(Song, related_name='media_uploads')
    url = models.URLField()
    title = models.CharField(max_length=200)
    media_type = models.CharField(max_length=3, choices=MEDIA_CHOICES)

    def __unicode__(self):
        return self.title




class Video(models.Model):
    song = models.ForeignKey(Song, related_name='videos')
    url = models.URLField()
    title = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title




