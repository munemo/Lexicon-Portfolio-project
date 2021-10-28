from django.contrib import admin
from .models import UserProfileInfo, SubscriberInfo, MailJobList
from . import models


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(SubscriberInfo)
admin.site.register(MailJobList)
admin.site.register(models.Contact, ContactAdmin)
