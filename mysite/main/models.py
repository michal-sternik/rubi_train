from django.db import models
from django.contrib.auth.models import User


class CubeType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class UserResults(models.Model):
    id = models.AutoField(primary_key=True)
    cubetype = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userResults", null=True)

    name = cubetype.name
    time = models.CharField(max_length=200)

    def __str__(self):
        return self.name