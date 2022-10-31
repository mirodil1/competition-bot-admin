from django.contrib import admin

from .models import TelegramUsers, InvitedUsers, Channels
# Register your models here.

class TelegramUsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'username', 'score', 'joined_date']
    list_filter = [ 'score', 'joined_date']


class InvitedUsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_offered', 'user_invited']


class ChannelsAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'status']

admin.site.register(TelegramUsers, TelegramUsersAdmin)
admin.site.register(InvitedUsers, InvitedUsersAdmin)
admin.site.register(Channels, ChannelsAdmin)