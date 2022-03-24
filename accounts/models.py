from django.db import models


class Account(models.Model):
    accountId = models.CharField(max_length=20, primary_key=True)
    username = models.CharField(max_length=30)
    profilePic = models.URLField(max_length=1000, default=" ")
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    medias = models.IntegerField(default=0)
    analyze = models.JSONField(default=dict)
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
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="media")
    source = models.URLField(max_length=1000, default= " ")
    type = models.CharField(max_length=20)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    analyze = models.JSONField(default=dict)
    caption = models.TextField(default=" ")
    hashtags = models.TextField(default=" ")
    resources = models.JSONField(default=dict)
    datePosted = models.DateTimeField()

    def __str__(self):
        return self.mediaId

