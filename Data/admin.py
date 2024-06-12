from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('wechat_name', 'message', 'send_time')
    search_fields = ('wechat_name', 'message')

admin.site.register(Message, MessageAdmin)