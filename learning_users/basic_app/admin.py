from django.contrib import admin
from basic_app.models import UserProfileInfo, SubscriberInfo

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(SubscriberInfo)
