from django.db import models

# Create your models here.

class Group(models.Model):

    id = models.IntegerField(primary_key=True)
    userId = models.ForeignKey('authsystem.User')
    name = models.CharField(max_length=30, null=False)
    picture = models.ImageField(null=True, default='safd')

    def __str__(self):

        return self.name

class UserGroupRequest(models.Model):

    id = models.IntegerField(primary_key=True)
    userId = models.ForeignKey('authsystem.User')
    groupId = models.ForeignKey('Group')
    time = models.TimeField(auto_now=True)

class UserGroupAssignment(models.Model):

    id = models.IntegerField(primary_key=True)
    userId = models.ForeignKey('authsystem.User')
    groupId = models.ForeignKey('Group')
    time = models.TimeField(auto_now=True)

class Message(models.Model):

    id = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=400)
    userId = models.ForeignKey('authsystem.User')
    time = models.TimeField(auto_now=True)

class UserMessageSeen(models.Model):

    id = models.IntegerField(primary_key=True)
    membershipId = models.ForeignKey('UserGroupAssignment')
    messageId = models.ForeignKey('Message')

