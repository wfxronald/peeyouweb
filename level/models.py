from django.db import models

class SongsCleared(models.Model):
    id = models.AutoField(primary_key=True)
    song = models.TextField()
    chatid = models.IntegerField()
    level = models.IntegerField()

    class Meta:
        db_table = 'SongsCleared'


class User(models.Model):
    chatid = models.IntegerField(primary_key=True)
    level = models.IntegerField()

    class Meta:
        db_table = 'User'

class TitleCard(models.Model):
    id = models.AutoField(primary_key=True)
    song = models.TextField()
    cut = models.TextField()
    image = models.TextField()

    class Meta:
        db_table = 'TitleCard'
        unique_together = (('song', 'cut'),)
