from django.db import models

# Create your models here.
class CubeType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Record(models.Model):
    cubetype = models.ForeignKey(CubeType, on_delete=models.CASCADE)

    name = cubetype.name
    time = models.TimeField()

    def __str__(self):
        return self.name + ", time: " + self.time