# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0002_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=200)),
                ('media_type', models.CharField(max_length=3, choices=[(b'VID', b'Video'), (b'MP3', b'MP3'), (b'PDF', b'PDF')])),
                ('song', models.ForeignKey(related_name='media_uploads', to='songs.Song')),
            ],
        ),
        migrations.AlterField(
            model_name='video',
            name='song',
            field=models.ForeignKey(related_name='videos', to='songs.Song'),
        ),
    ]
