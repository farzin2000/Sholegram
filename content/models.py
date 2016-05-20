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

    def __str__(self):

        return self.userId+str("->")+self.groupId.name

class UserGroupAssignment(models.Model):

    id = models.IntegerField(primary_key=True)
    userId = models.ForeignKey('authsystem.User')
    groupId = models.ForeignKey('Group')
    time = models.TimeField(auto_now=True)

    def __str__(self):

        return self.userId.user.username+str("->")+self.groupId.name


class Message(models.Model):

    id = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=400)
    membershipId = models.ForeignKey('UserGroupAssignment')
    time = models.TimeField(auto_now=True)

    def __str__(self):

        return self.content[:5]+str("->")+str("(")+self.membershipId.userId.user.username+str("->")+self.membershipId.groupId.name+str(")")

class UserMessageSeen(models.Model):

    id = models.IntegerField(primary_key=True)
    membershipId = models.ForeignKey('UserGroupAssignment')
    messageId = models.ForeignKey('Message')

