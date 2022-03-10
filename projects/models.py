from django.db import models
from django.contrib.auth.models import User
from django.utils.http import int_to_base36
from accounts.models import Account
import uuid

def idgen():
    return int_to_base36(uuid.uuid4().int)[:20]

class Project(models.Model):
    projectId = models.CharField(max_length=20, primary_key=True, default=idgen)
    projectName = models.CharField(max_length=20)
    projectOwner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    projectSize = models.IntegerField(default=25)
    projectGuests = models.ManyToManyField(User, related_name="guests")
    projectAccounts = models.ManyToManyField(Account, "accounts")

    def __str__(self):
        return self.projectId