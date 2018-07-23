from django.conf.urls import include, url
from django.contrib import admin
from sprof import urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'kblog.views.home', name='home'),
    url(r'', include('sprof.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
