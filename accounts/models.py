from django.db import models


class Account(models.Model):
    accountId = models.CharField(max_length=20, primary_key=True)
    username = models.CharField(max_length=30)
    followers = models.JSONField(default=dict)
    following = models.JSONField(default=dict)
    medias = models.JSONField(default=dict)
    avLikes = models.IntegerField(default=0)
    avComments = models.IntegerField(default=0)
    avViews = models.IntegerField(default=0)
    rankLikes = models.IntegerField(default=0)
    rankComments = models.IntegerField(default=0)
    rankViews = models.IntegerField(default=0)
    isVerified = models.BooleanField(default=False)
    bio = models.TextField(default=" ")
    hashtags = models.TextField(default=" ")

    def __str__(self):
        return self.username



class Media(models.Model):
    mediaId = models.CharField(primary_key=True, max_length=20, default=" ")
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    likes = models.JSONField(default=dict)
    views = models.JSONField(default=dict)
    comments = models.JSONField(default=dict)
    caption = models.TextField(default=" ")
    hashtags = models.TextField(default=" ")
    datePosted = models.DateTimeField()

    def __str__(self):
        return self.mediaId

