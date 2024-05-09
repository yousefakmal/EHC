from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(SiteUser)
admin.site.register(Ticket)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('MessageSender', 'Message_date', 'Message')
    list_filter = ('MessageSender', 'Message_date')
    search_fields = ('MessageSender', 'Message')

admin.site.register(Message, MessageAdmin)
admin.site.register(feedback)
