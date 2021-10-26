from django.conf.urls import url 
from basic_app import views
from django.conf import settings
from django.views.static import serve

app_name = 'basic_app'

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^portfolio/$', views.portfoliopage, name='portfolio'),
    url(r'^list_profiles/$', views.list_profiles, name='list_profiles'),
    url(r'^subscribe/$', views.subscribe, name='subscribe'),
    url(r'^list_subscribers/$', views.list_subscribers, name='list_subscribers'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^mail_joblist/$', views.mail_joblist, name='mail_joblist'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
]
