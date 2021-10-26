from django.contrib import admin
from basic_app.models import UserProfileInfo, SubscriberInfo, Contact, MailJobList
from basic_app import models

# Kash's class
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(SubscriberInfo)
admin.site.register(MailJobList)

## Kash added me
admin.site.register(models.Contact, ContactAdmin)
