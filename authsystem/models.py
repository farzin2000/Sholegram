from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):

    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User)
    gender = models.CharField(max_length=10)
    avatar = models.ImageField(null=True,default='528675-roger-federer.jpg')


    def __str__(self):

        return self.user.username