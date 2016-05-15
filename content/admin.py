from django.contrib import admin
from content.models import Message, Group, UserGroupAssignment, UserMessageSeen, UserGroupRequest
# Register your models here.

admin.site.register(Message)
admin.site.register(Group)
admin.site.register(UserGroupAssignment)
admin.site.register(UserMessageSeen)
admin.site.register(UserGroupRequest)